import os
import time
import unittest
from HTMLTestReportCN import HTMLTestRunner
from POM.stmp.send_email import mail


class report:
    def create_report(self):
        report_path = 'report/'
        if not os.path.exists(report_path):
            os.mkdir(report_path)

        now = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
        report_file = report_path + now + 'result.html'
        case_dir = r'C:\Code\pythonProject\pythonProject\test03\POM\cases'
        case_tests = unittest.defaultTestLoader.discover(case_dir, pattern='test_case.py', top_level_dir=r'C:\Code\pythonProject\pythonProject\test03')
        with open(report_file, 'wb') as fp:
            runner = HTMLTestRunner(stream=fp, title='加入购物车流程测试报告', description='实现加入购物车自动化流程测试报告')
            runner.run(case_tests)

    def new_report(self):
        test_report = r'C:\Code\pythonProject\pythonProject\test03\POM\suit_report\report'
        list = os.listdir(test_report)
        list.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))
        file_new = os.path.join(test_report, list[-1])
        return file_new


if __name__ == '__main__':
    runner = report()
    runner.create_report()
    file_new = runner.new_report()
    mail().send_email(file_new)
