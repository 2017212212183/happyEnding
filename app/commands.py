from datetime import datetime
import click

from app import app, db
from app.models import users, User, articles, Article


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息


# 虚拟数据
@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()
    # 用户表
    for m in users:
        user = User(email=m['email'], password=m['password'], head=m['head'], isAdmin=m['isAdmin'],
                    description=m['description'], time=datetime.now())
        db.session.add(user)
    # 文章表
    for m in articles:
        article = Article(articleId=m['articleId'], title=m['title'], Author=m['Author'], type_id=m['type_id'],
                          text=m['text'], image=m['image'],
                          modified_date=datetime.now(), thumbsUp=m['thumbsUp'], eyeOpen=m['eyeOpen'])
        db.session.add(article)
    db.session.commit()
    click.echo('Done.')
