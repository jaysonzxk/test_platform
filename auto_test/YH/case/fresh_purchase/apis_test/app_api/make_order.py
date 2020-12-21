from auto_test.YH.common.base import get_response
from auto_test.YH.common.logger import Log
from auto_test.YH.case.fresh_purchase.apis_test.app_api.get_key import getKey
from auto_test.YH.test_data.read_data import get_test_data
from auto_test.YH.case.fresh_purchase.apis_test.app_api.app_login import getAppToken



class makeOrder(object):
    def __init__(self):
        self.log = Log()  # 初始化日志
        self.token = getAppToken().get_token()  # 获取token
        self.key = getKey().get_key()  # 获取key
        self.test_data = get_test_data('/fresh_data.xlsx', 'app', 2)  # 初始化测试数据

    def get_order(self):
        """
        制单
        :return:
        """
        headers = eval(self.test_data.get('header'))
        headers['login-token'] = getAppToken().get_token()
        url = self.test_data.get('route') + self.key
        try:
            res = get_response(url, self.test_data.get('method'),
                               data=self.test_data.get('data').encode('utf-8'),
                               headers=headers)
            return res
        except Exception as e:
            self.log.error('请求异常%s' % e)


