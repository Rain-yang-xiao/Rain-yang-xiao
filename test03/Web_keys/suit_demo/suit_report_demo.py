import os
import time
import unittest
from HTMLTestReportCN import HTMLTestRunner
from Web_keys.stmp_demo.send_email_demo import Mail



class TestRunner:
    def run_report(self):
        # 指定存储生成报告的路径，若不存在就创建
        print('-------')
        report_path = 'report/'
        if not os.path.exists(report_path):
            os.mkdir(report_path)

        now = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
        report_file = report_path + now + 'result.html'
        fp = open(report_file, 'wb')
        # case_path = os.path.join(os.path.dirname(os.path.abspath()))
        # print(os.path.dirname(os.path.abspath())+'-------')
        # print(case_path)
        case_dir = '../unittest_demo'
        tests = unittest.defaultTestLoader.discover(case_dir, pattern='test_demo.py', top_level_dir=r'C:\Code\pythonProject\pythonProject\test03')
        runner = HTMLTestRunner(stream=fp, title='加入购物车流程测试报告', description='实现加入购物车自动化流程测试报告')
        runner.run(tests)
        fp.close()

    def new_report(self):
        test_report = r'C:\Code\pythonProject\pythonProject\test03\Web_keys\suit_demo\report'
        #  获取目录下所有的文件
        list = os.listdir(test_report)
        # 按时间排序测试报告
        list.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))
        file_new = os.path.join(test_report, list[-1])
        return file_new


if __name__ == '__main__':
      runner = TestRunner()
      runner.run_report()
      file_new = runner.new_report()
      mail = Mail()
      mail.send_email(file_new)





