from selenium import webdriver


class chrome_options:
    def options(self):
        # 创建options对象
        options = webdriver.ChromeOptions()
        # 去掉默认的自动化提示
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 窗体最大化
        options.add_argument('start-maximized')
        # 添加配置去掉密码管理弹窗
        prefs = {}
        prefs['credentials_enable_service'] = False
        prefs['profice.password_manager_enabled'] = False
        options.add_experimental_option('prefs', prefs)

        return options
