from datetime import datetime
from flask import render_template, request, redirect, url_for, make_response, flash
from flask_mail import Message
from app import app, db
from app.models import Article, User, PostForm, mymap, li
from app.templates.module.function import createCode, checkEmail, checkCode, checkPassword


@app.route('/')
@app.route('/home')
@app.route('/index')
def Home():
    techitem = Article.query.filter(Article.type_id == 1).order_by(-Article.modified_date).limit(4).all()
    eyesitem = Article.query.filter(Article.type_id == 2).order_by(-Article.modified_date).limit(2).all()
    lookitem = Article.query.filter(Article.type_id == 2).order_by(-Article.modified_date).limit(2).all()
    return render_template('home.html', techitems=techitem, eyesitems=eyesitem, lookitems=lookitem)


# 登陆页面
@app.route('/login', methods=['GET', 'POST'])
def login():
    # 区分处理请求
    if request.method == 'GET':  # 判断是否是 POST 请求
        techitem = Article.query.filter(Article.type_id == 1).order_by(-Article.modified_date).limit(4).all()
        eyesitem = Article.query.filter(Article.type_id == 2).order_by(-Article.modified_date).limit(2).all()
        lookitem = Article.query.filter(Article.type_id == 2).order_by(-Article.modified_date).limit(2).all()
        return render_template('login.html', techitems=techitem, eyesitems=eyesitem, lookitems=lookitem)
    else:
        # 获取表单数据
        email = request.form.get('user')
        password = request.form.get('password')
        # 验证数据
        if not email or not password:
            print('请填写完整')
            return redirect(url_for('login'))  # 重定向回主页
        # 查询数据库
        user = User.query.filter_by(email=email, password=password)
        # 用户存在
        if user.count():
            resp = make_response("存储cookie")
            resp.set_cookie('head', user[0].head)
            return redirect(url_for('Home'))  # 重定向回主页
        else:
            print('用户名密码错误或者用户不存在')  # 显示错误提示
            return redirect(url_for('login'))  # 重定向回主页


# 发送邮件
@app.route('/email', methods=['POST'])
def email():
    data = request.form
    global genertCode
    genertCode = createCode()
    print(genertCode)
    nowEmail = data['email']
    print(nowEmail)
    msg = Message('猿学习用户注册通知', sender='1049668876@qq.com', recipients=[nowEmail])
    msg.body = '注册验证码： ' + genertCode
    app.mail.send(msg)
    return "email"


# # 注册页面
@app.route('/register', methods=['GET', 'POST'])
def register():
    # 区分处理请求
    if request.method == 'GET':  # 判断是否是 POST 请求
        techitem = Article.query.filter(Article.type_id == 1).order_by(-Article.modified_date).limit(4).all()
        eyesitem = Article.query.filter(Article.type_id == 2).order_by(-Article.modified_date).limit(2).all()
        lookitem = Article.query.filter(Article.type_id == 2).order_by(-Article.modified_date).limit(2).all()
        return render_template('register.html', techitems=techitem, eyesitems=eyesitem, lookitems=lookitem)
    else:
        # 获取表单数据
        email3 = request.form.get('email1')
        password3 = request.form.get('password1')
        repassword = request.form.get('rePassword')
        code = request.form.get('code')

        print(email3, password3, repassword, code)
        # 验证数据
        try:
            checkEmail(email3)
            checkCode(code, genertCode)
            checkPassword(password3, repassword)

            # 查询数据库
            user = User.query.filter_by(email=email3)
            if user.count():
                print('用户已存在')  # 显示错误提示
                return redirect(url_for('register'))  # 重定向回主页
            else:
                # 写入数据库
                user = User(email=email3, password=password3, head='../static/images/head.jpeg', isAdmin=False,
                            description="个性签名", time=datetime.now())
                db.session.add(user)  # 添加到数据库会话
                db.session.commit()  # 提交数据库会话
                print('添加用户完成')  # 显示错误提示
                return redirect(url_for('login'))  # 重定向回主页
        except Exception as err:
            return redirect(url_for('register'))


# 文章页面
@app.route('/mainPage/<id>', methods=['GET', 'POST'])
def mainPage(id):
    type = mymap[id]
    if id == 'about':
        return "about"
    items = Article.query.filter(Article.type_id == type).all()
    data1 = Article.query.filter(Article.type_id == type).order_by(-Article.eyeOpen).all()
    data2 = Article.query.filter(Article.type_id == type).order_by(Article.thumbsUp).all()
    return render_template('pageAll.html', bgURL=li[type - 1], items=items, article1=data1,
                           article2=data2)


# 管理员控制台
@app.route('/admin')
def admin():
    user = User.query.all()  # 读取用户记录
    return render_template('admin.html', user=user)


@app.route('/mainPage/keySearch', methods=['GET', 'POST'])
def Search():
    key = request.form.get('keySearch')
    searchLooks = Article.query.filter(Article.article.ilike("%" + key + "%")).all()
    return render_template('pageAll.html', bgURL='../static/images/bg2.jpg', looks=searchLooks)


# markdown文章添加
@app.route('/addArticle', methods=['POST', 'GET'])
def test_1():
    form = PostForm()
    return render_template('test_1.html', form=form)


# 文章编辑
@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    form = PostForm()
    if form.validate_on_submit():
        article = Article.query.filter(Article.articleId == id).first()
        article.title = form.title.data
        article.type_id = form.type_id.data
        article.text = form.text.data
        # 修改数据库
        db.session.commit()
        user = User.query.filter(User.email == article.Author).first()
        return render_template('articlePage.html', bgURL=li[article.type_id - 1], article=article, image=user.head)
    return render_template('test_1.html', form=form)


# 删除按钮
@app.route('/deleteId/<int:id>', methods=['POST'])  # 限定只接受 POST 请求
def deleteId(id):
    article = Article.query.get_or_404(id)  # 获取电影记录
    db.session.delete(article)  # 删除对应的记录
    db.session.commit()  # 提交数据库会话
    flash('Item deleted.')
    return redirect(url_for("mainPage", id=article.type_id))


# 编辑文章
@app.route('/editId/<int:id>', methods=['POST', 'GET'])  # 限定只接受 POST 请求
def editId(id):
    article = Article.query.filter(Article.articleId == id).first()
    form = PostForm()
    form.title.data = article.title
    form.text.data = article.text
    form.type_id.data = article.type_id
    return render_template('test_1.html', form=form, id=article.articleId)


# 添加文章后回显
@app.route('/parse')
def parse():
    global markdown_text
    return render_template('parse.html', markdown=markdown_text)


# 浏览文章
@app.route('/scanArticle/<int:id>')
def scanArticle(id):
    article = Article.query.filter(Article.articleId == id).first()
    user = User.query.filter(User.email == article.Author).first()
    return render_template('articlePage.html', bgURL=li[article.type_id - 1], article=article, image=user.head)


@app.route('/userInfo')
def info():
    a = {'email': "1049668876@qq.com", 'description': "我凯爷最强", 'date': datetime.now()}
    return render_template('userInfo.html', user=a)
