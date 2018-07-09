# coding=utf-8
import requests


def renren_login():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    }
    login_url = 'http://www.renren.com/PLogin.do'
    # 3.拼接登录参数
    login_data = {
        'email': "15036292090",
        'password': 'anjing201402..'
    }

    # 4.发送登录请求post session对象自动保存cookie
    session = requests.session()
    session.post(login_url, headers=headers, data=login_data)

   # 5.如果成功 生成cookie
    profile_url = 'http://www.renren.com/919543526/profile'

    # 发送请求GET
    data = session.get(profile_url, headers=headers).content.decode()

    # 写入本地
    with open('renren02.html', 'w', encoding='utf-8') as f:
        f.write(data)


if __name__ == '__main__':
    renren_login()










