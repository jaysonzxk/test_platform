import time
import unittest
from ddt import ddt, data, unpack
from common.logger import Log
from common.base import get_response
from common.pc_login import getPcToken
from test_data.read_data import get_test_data, get_expect

expect_data = get_expect(('/space_data.xlsx', 'pc', 0), 'expect', ('code', 'message'))


@ddt
class testQueryList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        初始化测试数据
        :return:
        """
        cls.log = Log()
        cls.token = getPcToken().get_token()
        cls.test_data = get_test_data('/space_data.xlsx', 'pc', 0)
        cls.url = cls.test_data.get('route')
        cls.headers = eval(cls.test_data.get('header'))
        cls.headers['login-token'] = cls.token
        cls.json_data = cls.test_data.get('data')
        cls.method = cls.test_data.get('method')
        cls.log.info('测试数据初始化完成')

    # @data(*)
    # @unpack
    @data(*get_expect(('/space_data.xlsx', 'pc', 0), 'expect', ('code', 'message')))
    def test_query_list(self, expect):
        """
        测试查询商品信息管理全部列表
        :param expect:[200000, 'success']
        :return:
        """
        res = get_response(self.url, self.method, data=self.json_data, headers=self.headers)
        self.log.info('----------测试开始----------')
        self.log.info('测试断言-->期望值[{}]'.format(expect))
        self.log.info('请求接口地址:{}'.format(self.url))
        self.log.info('请求方法:{}'.format(self.method))
        self.log.info('请求头部:{}'.format(self.headers))
        self.log.info('请求参数:{}'.format(self.json_data))
        self.log.info('========================================================')
        self.log.info('响应结果:{}'.format(res.json()))
        self.assertIn(expect, [res.json()['code'], res.json()['message']],
                      msg='测试失败，失败原因，期望值{} not in 返回值{}中'.format(expect, res.json()))
        self.log.info('检查断言[{}]通过'.format(expect))
        self.log.info('---------测试结束----------')

    @classmethod
    def tearDownClass(cls):
        cls.log.info('测试结束，测试数据已经清除')


if __name__ == '__main__':
    unittest.main()
