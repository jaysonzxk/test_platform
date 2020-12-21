from auto_test.YH.case.fresh_purchase.apis_test.app_api.make_order import makeOrder
from auto_test.YH.test_data.read_data import get_test_data


def get_expect(args, expect_name, expect_key):
    """
    获取期望值
    :param args: 元组：测试文件路径，sheet名称，数字n
    :param expect_name: 表格头部key
    :param expect_key: 期望值的key
    :return:
    """
    expect = get_test_data(*args).get(expect_name)
    expect_list = [eval(expect).get(expect_key[0]), eval(expect).get(expect_key[1])]
    return expect_list


def get_pay_pwd(args, key, status):
    """
    获取一条用例不同场景测试数据--支付密码
    :param args: 测试数路径
    :param key: 测试数据对应的key-->data
    :param status:
    :return:
    """
    pay_data = eval(get_test_data(*args).get(key))

    # 支付密码为空
    if status == 0:
        pay_data['payPwd'] = ''
        pay_data['orderNo'] = makeOrder().get_order().json()['result']['applyOrderNo']
        return pay_data, '参数错误', '支付密码为空'
    # 支付密码错误
    if status == 1:
        pay_data['payPwd'] = '111111111'
        pay_data['orderNo'] = makeOrder().get_order().json()['result']['applyOrderNo']
        return pay_data, '参数校验异常', '支付密码错误'
    # 申请单号为空
    if status == 2:
        pay_data['orderNo'] = ''
        return pay_data, '参数错误', '申请单号为空'
    # 申请单号错误
    if status == 3:
        pay_data['orderNo'] = '22222222'
        return pay_data, '没有待支付的申请单，确认付款方式是否为现付', '申请单号错误'
    # 正常支付
    if status == 4:
        pay_data['orderNo'] = makeOrder().get_order().json()['result']['applyOrderNo']
        return pay_data, 'success', '正常支付'
