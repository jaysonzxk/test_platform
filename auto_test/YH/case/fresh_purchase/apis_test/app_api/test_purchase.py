import unittest
from auto_test.YH.case.fresh_purchase.apis_test.app_api.get_data import get_expect
from auto_test.YH.common.logger import Log
from auto_test.YH.case.fresh_purchase.apis_test.app_api.req_api import purchaseOrder
from ddt import ddt, data



@ddt
class testPurchase(unittest.TestCase):
    """
    测试制单接口
    """
    @classmethod
    def setUpClass(cls):
        """
        测试数据初始化
        :return:
        """
        cls.log = Log()  # 初始化日志
        cls.res = purchaseOrder('/fresh_data.xlsx', 'app', 2).purchase_order()  # 调用制单接口
        # cls.log.info('测试数据初始化完成')

    @data(*get_expect(('/fresh_data.xlsx', 'app', 2), 'expect', ('code', 'message')))
    def test_purchase(self, expect):
        """
        测试制单接口
        :return:
        """
        self.log.info('----------测试开始----------')
        self.log.info('测试断言-->期望值[{}]'.format(expect))
        self.assertIn(expect, [self.res.json()['code'], self.res.json()['message']],
                         msg='测试不通过，失败原因：%s not in %s' %
                             (expect, [self.res.json()['code'], self.res.json()['message']]))
        self.log.info('请求接口:{}'.format(self.res.url))
        self.log.info('请求方法:{}'.format(self.res.request.method))
        self.log.info('请求参数:{}'.format(self.res.request.body))
        self.log.info('=================================================')
        self.log.info('响应结果:{}'.format(self.res.json()))
        self.log.info('检查断言[{}]通过'.format(expect))
        self.log.info('---------测试结束----------')


    @classmethod
    def tearDownClass(cls):
        # cls.log.info('测试结束，测试数据已经清除')
        pass


if __name__ == '__main__':
    unittest.main()