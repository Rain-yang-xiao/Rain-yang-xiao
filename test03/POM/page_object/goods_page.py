from time import sleep

from selenium.webdriver.common.by import By

from POM.base.base_object import Base


class goods(Base):
    url = Base.url + '?s=/index/goods/index/id/2.html'
    menu = (By.XPATH, '//*[@data-value="套餐一"]')
    color = (By.XPATH, '//*[@data-value=金色""]')
    capacity = (By.XPATH, '//*[@data-value="32G"]')
    button = (By.XPATH, '//*[@title="加入购物车"]')

    def goods_select(self):
        self.open(self.url)
        self.click_(self.menu)
        sleep(1)
        self.click_(self.color)
        sleep(1)
        self.click_(self.capacity)
        self.click_(self.button)

