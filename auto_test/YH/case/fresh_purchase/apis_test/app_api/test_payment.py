import json
import unittest
from ddt import data, ddt
from auto_test.YH.common.base import get_response
from auto_test.YH.test_data.read_data import get_test_data
from auto_test.YH.case.fresh_purchase.apis_test.app_api.app_login import getAppToken
from auto_test.YH.case.fresh_purchase.apis_test.app_api.get_data import get_pay_pwd
from auto_test.YH.common.logger import Log


@ddt
class testPayment(unittest.TestCase):
    """
    测试支付场景
    """
    @classmethod
    def setUpClass(cls):
        cls.log = Log()
        cls.test_data = get_test_data('/fresh_data.xlsx', 'app', 3)
        cls.url = cls.test_data.get('route')
        cls.headers = eval(cls.test_data.get('header'))
        cls.headers['login-token'] = getAppToken().get_token()
        cls.method = cls.test_data.get('method')
        # cls.log.info('测试数据初始化完成')

    @data(*[get_pay_pwd(('/fresh_data.xlsx', 'app', 3), 'data', 0), get_pay_pwd(('/fresh_data.xlsx', 'app', 3), 'data', 1),
          get_pay_pwd(('/fresh_data.xlsx', 'app', 3), 'data', 2), get_pay_pwd(('/fresh_data.xlsx', 'app', 3), 'data', 3),
          get_pay_pwd(('/fresh_data.xlsx', 'app', 3), 'data', 4)])
    def test_payment(self, test_data):
        """
        测试支付场景
        :param test_data:
        :return:
        """
        res = get_response(self.url, self.method, data=json.dumps(test_data[0]), headers=self.headers)
        self.log.info('----------测试开始----------')
        self.log.info('测试场景：[{}]'.format(test_data[2]))
        self.log.info('测试断言-->期望值/校验值[{}]'.format(test_data[1]))
        self.log.info('请求参数:{}'.format(test_data[0]))
        self.assertIn(test_data[1], res.json()['message'], msg='测试不通过，失败原因：%s not in %s' %
                             (test_data[1], res.json()['message']))
        self.log.info('请求接口:{}'.format(self.url))
        self.log.info('请求方法:{}'.format(self.method))
        self.log.info('响应结果:{}'.format(res.json()))
        self.log.info('测试断言[{}]通过'.format(test_data[1]))
        self.log.info('----------测试通过----------')
        self.log.info('=======================================================')

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()