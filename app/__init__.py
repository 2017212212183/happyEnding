import os
import sys

from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
from flaskext.markdown import Markdown
from app.templates.module.function import checkEmail, checkCode, checkPassword, createCode
from flask_bootstrap import Bootstrap

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '1049668876@qq.com'  # 邮箱账号
app.config['MAIL_PASSWORD'] = 'hdhooqrbmdpbbdhf'  # QQ邮箱授权码

mail = Mail(app)

bootstrap = Bootstrap(app)
Markdown(app)
db = SQLAlchemy(app)

from app import views, errors, commands
