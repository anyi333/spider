import requests
import json

class FanyiSpider(object):
    def fanyi(self):
        # 1.目标url
        url = 'http://fanyi.baidu.com/basetrans'
        headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36"}
        word = input("请输入要翻译的内容：")
        # 2.拼接参数
        data = {
            'query': word,
            'from': 'zh',
            'to': 'en'
        }
        # 3.发送post请求
        response = requests.post(url, data=data,headers=headers)
        res_data = response.content.decode()

        # 4.解析数据 jsonstr --> dict
        dict_data = json.loads(res_data)
        result = dict_data["trans"][0]["result"][0][1]
        print("翻译的结果是：{}".format(result))

if __name__ == '__main__':
    tool = FanyiSpider()
    tool.fanyi()