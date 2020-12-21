from auto_test.YH.common.base import get_response
from auto_test.YH.test_data.read_data import get_test_data
from auto_test.YH.common.logger import Log


class getAppToken(object):
    def __init__(self):
        self.log = Log()

    # @staticmethod
    def get_token(self):
        """
        获取app登录token
        :return:token
        """
        try:
            test_data = get_test_data('/fresh_data.xlsx', 'app', 0)
            res = get_response(test_data['route'], test_data['method'],
                               data=test_data['data'], headers=eval(test_data['header']))
            return res.json()['response']['token']
        except Exception as e:
            self.log.error('获取token出现异常:{}'.format(str(e)))
