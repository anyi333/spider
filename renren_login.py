# coding=utf-8
import requests


def renren_login():
    # 1.url
    profile_url = 'http://www.renren.com/919543526/profile'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    }
    # 2.发送cookie参数传递字典
    cook_str = 'anonymid=jje86ntn8fa695; depovince=BJ; jebecookies=03735b8b-20b0-4f7c-8697-d2776e4380cc|||||; _r01_=1; JSESSIONID=abcUQcXcDWCkTh8268_rw; ick_login=526f2a53-3971-4f20-96a5-13debf107186; _de=19A79B7F400350DCD89AADF4B0420A80; p=2378ad0e5cd69c4be70d9c938361779c1; first_login_flag=1; ln_uact=15036292090; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=0cbbb1d7ca13f838baf7af2655464f3f1; societyguester=0cbbb1d7ca13f838baf7af2655464f3f1; id=965217371; xnsid=810bff12; loginfrom=syshome; jebe_key=8b472b96-6263-457c-b600-d0d66a50a080%7Cdaf4c749e889f038cd159748d567de3f%7C1531138293613%7C1%7C1531138298133; wp_fold=0; _ga=GA1.2.1506886064.1531138413; _gid=GA1.2.439960573.1531138413; XNESSESSIONID=20f35c5b42ee; WebOnLineNotice_965217371=1'
    # 3.将cookie字符串转成字典
    # # 分割字符串
    # cook_list = cook_str.split('; ')
    # # 遍历拼接
    # dict_cook = {}
    # for cook in cook_list:
    #     dict_cook[cook.split('=')[0]] = cook.split('=')[1]

    # 列表推导式
    dict_tow_cook = {i.split('=')[0]: i.split('=')[1] for i in cook_str.split('; ')}
    print(dict_tow_cook)
    cook_dict = {
        "anonymid": "jje86ntn8fa695",
        "depovince": "BJ",
        "jebecookies": "03735b8b-20b0-4f7c-8697-d2776e4380cc|||||",
        "_r01_": "1",
        "JSESSIONID": "abcUQcXcDWCkTh8268_rw",
        "ick_login": "526f2a53-3971-4f20-96a5-13debf107186",
        "_de": "19A79B7F400350DCD89AADF4B0420A80",
        "p": "2378ad0e5cd69c4be70d9c938361779c1",
        "first_login_flag": "1",
        "ln_uact": "15036292090",
        "ln_hurl": "http://head.xiaonei.com/photos/0/0/men_main.gif",
        "t": "0cbbb1d7ca13f838baf7af2655464f3f1",
        "societyguester": "0cbbb1d7ca13f838baf7af2655464f3f1",
        "id": "965217371",
        "xnsid": "810bff12",
        "loginfrom": "syshome",
        "jebe_key": "8b472b96-6263-457c-b600-d0d66a50a080%7Cdaf4c749e889f038cd159748d567de3f%7C1531138293613%7C1%7C1531138298133",
        "wp_fold": "0",
        "_ga": "GA1.2.1506886064.1531138413",
        "_gid": "GA1.2.439960573.1531138413",
        "XNESSESSIONID=20f35c5b42eeWebOnLineNotice_965217371": "1",
    }

    # 发送请求get
    data = requests.get(profile_url, headers=headers, cookies=cook_dict).content.decode()
    # 3.写入本地
    with open('renren01.html', 'w', encoding='utf-8') as f:
        f.write(data)


if __name__ == '__main__':
    renren_login()










