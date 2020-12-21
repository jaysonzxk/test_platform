import requests
from auto_test.YH.common.logger import Log
# from common import cof


class MyRequestMethod(object):
    def __init__(self):
        self.log = Log()

    def get(self, url, **kwargs):
        """
        封装get方法
        :param url:
        :param kwargs:
        :return:
        """
        params = kwargs.get("params")
        headers = kwargs.get("headers")
        try:
            res = requests.get(url, params=params, headers=headers)
            # self.log.info("响应的内容：%s" %res.json())
            # self.log.info("返回的状态码：%s" % res.status_code)
            return res
        except Exception as e:
            self.log.error("get请求错误: %s" %e)

    def post(self, url, **kwargs):
        """
        封装post方法
        :param url:
        :param kwargs:
        :return:
        """
        params = kwargs.get("params")
        data = kwargs.get("data")
        json = kwargs.get("json")
        files = kwargs.get("files")
        header = kwargs.get("headers")
        try:
            res = requests.post(url, params=params, data=data, json=json, files=files, headers=header)
            # self.log.info("响应的内容：%s" %res.json())
            # self.log.info("返回的状态码：%s" % res.status_code)
            return res
        except Exception as e:
            self.log.error("post请求错误: %s" %e)
