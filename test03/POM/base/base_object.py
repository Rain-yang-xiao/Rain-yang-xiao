


class Base:
    url = 'http://39.98.138.157/shopxo/index.php'
    def __init__(self, drive):
        self.drive = drive

    # 输入url
    def open(self, url):
        self.drive.get(url)

    # 元素定位
    def locator(self, loc):
       return self.drive.find_element(*loc)

    # 输入内容
    def input_(self, loc, text):
        self.locator(loc).send_keys(text)

    # 点击操作
    def click_(self, loc):
        self.locator(loc).click()
