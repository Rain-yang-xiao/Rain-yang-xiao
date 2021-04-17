from selenium import webdriver
from selenium.webdriver.common.by import By

from POM.base.base_object import Base


class Login(Base):

    url = Base.url + '?s=/index/user/logininfo.html'
    username = (By.XPATH, '//*[@placeholder="用户名/手机/邮箱"]')
    password = (By.XPATH, '//*[@placeholder="登录密码"]')
    button = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')

    def login_page(self, username, password):
        self.open(self.url)
        self.input_(self.username, username)
        self.input_(self.username, password)
        self.click_(self.button)



