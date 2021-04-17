import threading

from Web_keys.suit_demo.suit_report_demo import TestRunner
from Web_keys.stmp_demo.send_email_demo import Mail
from POM.suit_report.create_report import report
from POM.stmp.send_email import mail


class Thread:

    def web_keys(self):
        runner = TestRunner()
        runner.run_report()
        runner.new_report()
        # file_new = runner.new_report()
        # mail = Mail()
        # mail.send_email(file_new)

    def POM(self):
        runner = report()
        runner.create_report()
        runner.new_report()
        # file_new = runner.new_report()
        # mail().send_email(file_new)

    def thread(self):
        th = []
        th.append(threading.Thread(target=self.POM))
        th.append(threading.Thread(target=self.web_keys))

        for t in th:
           t.start()

if __name__ == '__main__':
    Thread().web_keys()