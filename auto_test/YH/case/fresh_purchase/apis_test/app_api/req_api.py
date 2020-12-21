import json

from ddt import ddt, data

from auto_test.YH.case.fresh_purchase.apis_test.app_api.get_data import get_pay_pwd
from auto_test.YH.common.base import get_response
from auto_test.YH.common.logger import Log
from auto_test.YH.case.fresh_purchase.apis_test.app_api.get_key import getKey
from auto_test.YH.test_data.read_data import get_test_data
from auto_test.YH.case.fresh_purchase.apis_test.app_api.app_login import getAppToken




class initializationData(object):
    def __init__(self, file_path, sheet_name, n):
        self.log = Log()  # 初始化日志
        self.token = getAppToken().get_token()  # 获取token
        self.key = getKey().get_key()  # 获取key
        self.test_data = get_test_data(file_path, sheet_name, n)  # 初始化测试数据



class purchaseOrder(initializationData):
    def purchase_order(self):
        """
        制单接口
        :return:
        """
        headers = eval(self.test_data.get('header'))
        headers['login-token'] = self.token
        url = self.test_data.get('route') + self.key
        try:
            res = get_response(url, self.test_data.get('method'),
                               data=self.test_data.get('data').encode('utf-8'),
                               headers=headers)
            return res
        except Exception as e:
            self.log.error('请求异常%s' % e)
