from auto_test.YH.common.base import get_response
from auto_test.YH.test_data.read_data import get_test_data
from auto_test.YH.common.logger import Log


class getPcToken(object):
    def __init__(self):
        self.log = Log()

    # @staticmethod
    def get_token(self):
        """
        获取PC登录token
        :return:token
        """
        try:
            test_data = get_test_data('/fresh_data.xlsx', 'pc', 0)
            # data_dict = dict(zip(test_data[0], test_data[1][0]))
            res = get_response(test_data.get('route'), test_data.get('method'),
                               data=test_data.get('data'), headers=eval(test_data.get('header')))
            token = res.json()['result']['loginToken']
            return token
        except Exception as e:
            self.log.error('出现异常:{}'.format(str(e)))