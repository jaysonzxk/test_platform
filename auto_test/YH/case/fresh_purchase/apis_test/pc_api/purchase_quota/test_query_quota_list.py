import time
import unittest
from ddt import ddt, data, unpack
from auto_test.YH.common.logger import Log
from auto_test.YH.common.base import get_response
from auto_test.YH.common.pc_login import getPcToken
from auto_test.YH.test_data.read_data import get_test_data


# @ddt
class testQueryQuotaList(unittest.TestCase):
    def setUp(self):
        self.log = Log()
        self.token = getPcToken().get_token()
        self.test_data = get_test_data('/fresh_data.xlsx', 'pc', 1)

    # @data(*get_test_data('/fresh_data.xlsx', 'pc', 1).get('expect'))
    def test_query_quota_list(self,):
        """
        测试获取额度维护全部列表
        expect: 期望值
        :return:
        """
        url = self.test_data.get('route')
        headers = eval(self.test_data.get('header'))
        headers['login-token'] = self.token
        data = self.test_data.get('data')
        res = get_response(url, self.test_data.get('method'),
                           data=data, headers=headers)
        print(res.json())
        print(get_test_data('/fresh_data.xlsx', 'pc', 1).get('expect'))
        # print(expect)
        # self.assertIn(expect, [res.json()['code'], res.json()['message']], True)


if __name__ == '__main__':
    unittest.main()