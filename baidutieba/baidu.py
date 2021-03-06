# coding=utf-8
# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests


class TiebaSpider(object):
    def __init__(self):
        self.tieba_name = input('请输入贴吧名字:')
        self.start_page = int(input('请输入开始页:'))
        self.end_page = int(input('请输入结束页:'))

        self.base_url = 'https://tieba.baidu.com/f?'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 1.发送请求
    def send_request(self, send_params):
        response = requests.get(self.base_url, headers=self.headers, params=send_params)
        data = response.content.decode()
        return data

    # 2.保存本地文件
    def save_data(self, data, page):
        file_path = 'Tieba/' + str(page) + '页.html'

        print('正在下载{}页...'.format(page))

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(data)
            print('保存完毕')

    # 3.调度
    def run(self):
        for page in range(self.start_page, self.end_page + 1):
            # 拼接参数
            params = {
                'kw': self.tieba_name,
                'pn': (page - 1) * 50
            }
            # 1.发送请求
            data = self.send_request(params)

            # 2.保存本地文件
            self.save_data(data, page)


if __name__ == '__main__':
    tool = TiebaSpider()
    tool.run()
