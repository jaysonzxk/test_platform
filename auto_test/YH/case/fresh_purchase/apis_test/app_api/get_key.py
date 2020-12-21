from auto_test.YH.common.base import get_response
from auto_test.YH.test_data.read_data import get_test_data
from auto_test.YH.common.logger import Log
from .app_login import getAppToken


class getKey(object):
    def __init__(self):
        self.log = Log()

    # @staticmethod
    def get_key(self):
        """
        获取key
        :return:key
        """
        try:
            test_data = get_test_data('/fresh_data.xlsx', 'app', 1)
            headers = eval(test_data.get('header'))
            headers['login-token'] = getAppToken().get_token()
            res = get_response(url=test_data.get('route'), method=test_data.get('method'), headers=headers)
            # self.log.info('请求获取key的地址:{}'.format(data_dict.get('route')))
            # self.log.info('请求方式:{}'.format(data_dict.get('method')))
            # self.log.info('请求头部:{}'.format(headers))
            # self.log.info('获取的key:{}'.format(res.json()['result']))
            return res.json()['result']
        except Exception as e:
            self.log.error('出现异常:{}'.format(str(e)))
