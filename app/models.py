from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired, length
from app import db


class PostForm(FlaskForm):
    title = StringField('Title',
                        [DataRequired('请输入文章标题'), length(max=50)],
                        render_kw={
                            "class": "form-control",
                            "placeholder": "请输入文章标题",
                            "required": 'required'  # 表示输入框不能为空，并有提示信息
                        }
                        )

    text = TextAreaField('Content', [DataRequired('请输入文章')])
    type_id = SelectField('type_id', coerce=int,
                          choices=[(1, '技术'), (2, '眼界'), (3, '形象')],
                          default=1)

    def __init__(self):
        super(PostForm, self).__init__()


# 表名将会是 user（自动生成，小写处理）
class User(db.Model):
    email = db.Column(db.String(20), primary_key=True)  # 主键
    password = db.Column(db.String(20))  # 密码
    head = db.Column(db.String(50), default="../static/images/default.png")  # 头像数据
    isAdmin = db.Column(db.Boolean)  # 是否管理员
    description = db.Column(db.String(200))  # 个性签名
    time = db.Column(db.DateTime, default=datetime.now)  # 上次登陆时间


# 文章类：
class Article(db.Model):
    articleId = db.Column(db.Integer, primary_key=True)  # 文章ID（主键）
    title = db.Column(db.String(50))  # 文章标题
    Author = db.Column(db.String(50))  # 文章标题
    type_id = db.Column(db.Integer)  # 文章类型({1,2,3})
    text = db.Column(db.TEXT)  # 文章内容
    modified_date = db.Column(db.DateTime, default=datetime.now)  # 文章更新时间
    thumbsUp = db.Column(db.Integer)  # 点赞数
    eyeOpen = db.Column(db.Integer)  # 浏览量
    image = db.Column(db.String(50))  # 文章图片


li = ["../static/images/bg.jpg", "../static/images/bg1.jpg", "../static/images/bg2.jpg"]
mymap = {"technplogy": 1, "horizons": 2, "looks": 3, "about": 4}

genertCode = "000000"

markdown_text = ''

articles = [
    {'articleId': 1, 'title': "听说程序员秃顶是尊贵身份的象征？1 ", 'Author': "1049668876@qq.com", 'type_id': 2,
     'text': '作为一名程序员必须知道的事情：女怕嫁错郎，男怕入错行，程序猿最怕就是选错语言！选择一门牛逼的编程语言是每一位程序员进入IT江湖的头等大事。为什么...',
     'image': '../static/images/addImg1.png', 'thumbsUp': 53451, "eyeOpen": 12},
    {'articleId': 2, 'title': "听说程序员秃顶是尊贵身份的象征？2 ", 'Author': "1049668876@qq.com", 'type_id': 3,
     'text': '作为一名程序员必须知道的事情：女怕嫁错郎，男怕入错行，程序猿最怕就是选错语言！选择一门牛逼的编程语言是每一位程序员进入IT江湖的头等大事。为什么...',
     'image': '../static/images/addImg1.png', 'thumbsUp': 53451, "eyeOpen": 12},
    {'articleId': 3, 'title': "听说程序员秃顶是尊贵身份的象征？3 ", 'Author': "1049668876@qq.com", 'type_id': 2,
     'text': '作为一名程序员必须知道的事情：女怕嫁错郎，男怕入错行，程序猿最怕就是选错语言！选择一门牛逼的编程语言是每一位程序员进入IT江湖的头等大事。为什么...',
     'image': '../static/images/addImg1.png', 'thumbsUp': 53451, "eyeOpen": 213},
    {'articleId': 4, 'title': "听说程序员秃顶是尊贵身份的象征？4 ", 'Author': "1049668876@qq.com", 'type_id': 2,
     'text': '作为一名程序员必须知道的事情：女怕嫁错郎，男怕入错行，程序猿最怕就是选错语言！选择一门牛逼的编程语言是每一位程序员进入IT江湖的头等大事。为什么...',
     'image': '../static/images/addImg1.png', 'thumbsUp': 53451, "eyeOpen": 31},
    {'articleId': 5, 'title': "听说程序员秃顶是尊贵身份的象征？5 ", 'Author': "1049668876@qq.com", 'type_id': 3,
     'text': '作为一名程序员必须知道的事情：女怕嫁错郎，男怕入错行，程序猿最怕就是选错语言！选择一门牛逼的编程语言是每一位程序员进入IT江湖的头等大事。为什么...',
     'image': '../static/images/addImg1.png', 'thumbsUp': 33, "eyeOpen": 234},
    {'articleId': 6, 'title': "听说程序员秃顶是尊贵身份的象征？6 ", 'Author': "1049668876@qq.com", 'type_id': 3,
     'text': '作为一名程序员必须知道的事情：女怕嫁错郎，男怕入错行，程序猿最怕就是选错语言！选择一门牛逼的编程语言是每一位程序员进入IT江湖的头等大事。为什么...',
     'image': '../static/images/addImg1.png', 'thumbsUp': 12, "eyeOpen": 124},
    {'articleId': 8, 'title': "hadoop分布式实验", 'Author': "1049668876@qq.com", 'type_id': 1,
     'text': 'hadoop 分布式实验......',
     'image': '../static/images/hadoop.jpg', 'thumbsUp': 53451, "eyeOpen": 12},
    {'articleId': 9, 'title': "Docker入门实践", 'Author': "1049668876@qq.com", 'type_id': 1,
     'text': 'Docker入门实践......',
     'image': '../static/images/Docker.jpg', 'thumbsUp': 53451, "eyeOpen": 12},
    {'articleId': 10, 'title': "深度解读比特币白皮书", 'Author': "1049668876@qq.com", 'type_id': 1,
     'text': '深度解读比特币白皮书......',
     'image': '../static/images/biteBi.jpg', 'thumbsUp': 53451, "eyeOpen": 12},
    {'articleId': 7, 'title': "阿里P8数据架构师顶级开发者说数据库", 'Author': "1049668876@qq.com", 'type_id': 1,
     'text': '阿里P8数据架构师顶级开发者说数据库......',
     'image': '../static/images/database.jpg', 'thumbsUp': 53451, "eyeOpen": 12}
]


# 全局的两个变量移动到这个函数内
users = [
    {'email': '1049668876@qq.com', 'password': '123', 'head': '../static/images/head.jpeg', 'isAdmin': True,
     'description': "我凯爷牛逼"},
    {'email': '3324791952@qq.com', 'password': '123', 'head': '../static/images/head.jpeg', 'isAdmin': False,
     'description': "我凯爷牛逼"},
]
