import unittest

from ddt import ddt, file_data

from Web_keys.Web_key.webkeys_demo import Webkeys

@ddt
class test(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = Webkeys('Chrome')

    def tearDown(self) -> None:
        self.driver.quit()


    @file_data('../Data/test_data.yaml')
    def test_01(self, **kwargs):
        self.driver.get(kwargs['url'])
        self.driver.click(**kwargs['login'])
        self.driver.input(**kwargs['username'])
        self.driver.input(**kwargs['password'])
        self.driver.click(**kwargs['button'])
        el = self.driver.assert_(**kwargs['asser_'])
        self.assertTrue(el)
        self.driver.input(**kwargs['search'])
        self.driver.click(**kwargs['click1'])
        self.driver.click(**kwargs['click2'])
        self.driver.switch_no_close()
        self.driver.click(**kwargs['click3'])
        self.driver.wait(kwargs['wait2'])
        self.driver.click(**kwargs['click4'])
        self.driver.wait(kwargs['wait3'])
        self.driver.click(**kwargs['click5'])
        self.driver.click(**kwargs['click6'])
        self.driver.assert_wait(**kwargs['assert_wait'])
        self.driver.click(**kwargs['click7'])
        self.driver.wait(kwargs['wait1'])








# if __name__ == '__main__':
#         unittest.main()
