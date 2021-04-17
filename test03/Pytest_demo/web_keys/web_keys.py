from selenium import webdriver
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

from Pytest_demo.chrome_options.options import Options

def browser(type_):
    try:
        driver = getattr(webdriver, type_)(options = Options().chrome_options())
    except Exception as e:
        print(e)
        driver = webdriver.Chrome(options= Options().chrome_options())
    return driver

class Webkeys:
    def __init__(self, type_):
        self.driver = browser(type_)
        self.driver.implicitly_wait(10)

    def open(self,url):
        self.driver.get(url)

    def locator(self, **kwargs):
        return self.driver.find_element(kwargs['name'], kwargs['value'])

    def input(self, **kwargs):
        self.locator(**kwargs).send_keys(kwargs['text'])

    def click(self, **kwargs):
        self.locator(**kwargs).click()

    def assert_(self, **kwargs):
        try:
            assert self.locator(**kwargs).text == kwargs['expect']
            return True
        except:
            return False

    def switch_no_close(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    def assert_wait(self, **kwargs):
        try:
            el = WebDriverWait(self.driver, kwargs['text'], 0.5).until(lambda el: self.locator(**kwargs))
            return el
        except:
            return False

    def wait(self, time):
        sleep(time)

    def quit(self):
        self.driver.quit()