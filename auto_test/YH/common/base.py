from auto_test.YH.common.requestMethod import MyRequestMethod
from auto_test.YH.common.logger import Log


def get_response(url, method, **kwargs):
    if method == "get":
       resp = MyRequestMethod().get(url, **kwargs)
    if method == "post":
        resp = MyRequestMethod().post(url, **kwargs)
    if method =="delete":
        pass
    if method =="put":
        pass
    return resp
