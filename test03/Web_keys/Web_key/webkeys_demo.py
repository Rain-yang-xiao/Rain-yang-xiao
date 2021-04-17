from selenium import webdriver
from time import sleep
from Web_keys.Chrome_options.chrome_options_demo import chrome_options
from selenium.webdriver.support.wait import WebDriverWait


def browser(type_):
    try:
        driver = getattr(webdriver, type_)(options = chrome_options().options())

    except Exception as e:
        print(e)
        driver = webdriver.Chrome(options = chrome_options().options())
    return driver


class Webkeys:
    def __init__(self, type_):
        self.driver = browser(type_)
        self.driver.implicitly_wait(10)

    # 输入url
    def get(self, url):
        self.driver.get(url)

    # 元素定位
    def locator(self, **kwargs):
        return self.driver.find_element(kwargs['name'], kwargs['value'])

    # 输入内容
    def input(self, **kwargs):
        self.locator(**kwargs).send_keys(kwargs['text'])

    # 点击操作
    def click(self, **kwargs):
        self.locator(**kwargs).click()

    # 断言操作
    def assert_(self, **kwargs):
        try:
            assert self.locator(**kwargs).text == kwargs['expect']
            return True
        except:
            return False

    # 切换句柄:不关闭旧窗体
    def switch_no_close(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

   # 显示等待
    def assert_wait(self, **kwargs):
        try:
            el = WebDriverWait(self.driver, kwargs['text'], 0.5).until(lambda el: self.locator(**kwargs))
            return el
        except:
            return False

   # 强制等待
    def wait(self, time):
        sleep(time)



    # 退出
    def quit(self):
        self.driver.quit()
