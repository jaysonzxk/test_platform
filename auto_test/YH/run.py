import unittest
import os
import time
import HTMLTestRunner


# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.abspath(__file__))


def add_case(product, module):
    """
    第一步：加载所有的测试用例
    :param rule:测试用例文件命令规则
    :param product:被测系统
    :param module:被测模块
    :return:
    """
    f_path = os.path.dirname(os.path.abspath(__file__))
    # 动态获取被测项目
    for root, dirs, files in os.walk(f_path):
        if product in root and root.endswith(module):
            case_path = root  # 需要执行用例文件夹
            discover = unittest.defaultTestLoader.discover(case_path,
                                                            pattern='test*',
                                                            top_level_dir=None)
            return discover


def run_case(all_case, reportName="report"):
    """
    第二步：执行所有的用例，并把结果写入HTML测试报告
    :param all_case:
    :param reportName:
    :return:
    """
    now = time.strftime("%Y%m%d%H%M%S")
    report_path = os.path.join(cur_path, reportName)  # 报告文件夹
    # 如果不存在就创建
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    report_abspath = os.path.join(report_path, now+"result.html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="API测试报告",
                                           description="用例执行情况")

    # 调用add_case返回值
    runner.run(all_case)  # discover
    fp.close()


def get_report_file(report_path):
    """
    第三步：获取最新的测试报告
    :param report_path:
    :return:
    """
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))
    print("最新测试报告: "+lists[-1])
    # 找到最新生成的测试报告
    reportfile = os.path.join(report_path, lists[-1])
    return reportfile



# if __name__ == "__main__":
# #     all_case = add_case('test*', 'fresh_purchase', 'app_api')   # 1 加载用例
# #     # 生成测试报告路径
# #     run_case(all_case)      # 2 执行用例
# #     report_path = os.path.join(cur_path, "report")   # 用例文件
# #     report_file = get_report_file(report_path)    # 3 获取最新测试报告
