import selenium.webdriver as webdriver


class WebDriverFactory:
    @staticmethod
    def get_driver(browser_name):
        if (browser_name == 'firefox'):
            return webdriver.Firefox()
        elif (browser_name == 'chrome'):
            return webdriver.Chrome()
        elif (browser_name == 'ie'):
            return webdriver.Ie()
        elif (browser_name == 'edge'):
            return webdriver.Edge()

        raise Exception("No such " + browser_name + " browser exists")