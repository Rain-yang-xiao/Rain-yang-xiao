import unittest

from ddt import file_data, ddt
from selenium import webdriver

from POM.log.log import Logger
from POM.page_object.goods_page import goods
from POM.page_object.login_page import Login
from POM.chrome_options.options import chrome_options


@ddt
class test_case(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Logger().print_log()
        cls.driver = webdriver.Chrome(options=chrome_options().options())
        cls.lg = Login(cls.driver)
        cls.gd = goods(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data/login_data.yaml')
    def test_01_login(self, **kwargs):
        # self.log.info('获取{0}内容成功，现在开始执行自动化测试.....'.format())
        self.lg.login_page(kwargs['username'], kwargs['password'])

    def test_02_addcart(self):
        self.gd.goods_select()

