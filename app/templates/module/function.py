import math
import random
import re


def checkEmail(email):
    print("checkEmial" + email)
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'
    if re.match(pattern, email) is not None:
        print('邮箱地址输入正确')
    else:
        print('邮箱地址输入错误')
        raise Exception("邮箱填写不正确")


def checkPassword(password, rePassword):
    if password == "" or rePassword == "":
        raise Exception("密码不能为空")
    if password != rePassword:
        raise Exception("两次密码不同")


def checkCode(code, ans):
    print("checkcode: " + code + ans)
    if code == "":
        raise Exception("验证码不能为空")
    if code != ans:
        raise Exception("验证码不正确")
    print("验证码正确")


def createCode():
    num = ""
    for i in range(6):
        num += str(random.randint(0, 9))
    return num
