from tests.pages import locators
from webdriver_factory import WebDriverFactory
from tests.pages.main_page import MainPage


class TestForgotPassword():
    driver = WebDriverFactory.get_driver('chrome')
    main_page = MainPage(driver)

    def test_setup(self):
        self.main_page.open_main_page()
        self.main_page.open_login_page()

    def test_(self):
        self.driver.find_element_by_xpath(locators.LINK_FORGOT_PASSW).click()
        # Verify that needed page is opened
        assert self.driver.find_element_by_xpath(locators.FORGOT_PASSWORD_PAGE_VALIDATION), \
            "The Password recovery page isn't opened"

    def test_teardown(self):
        self.driver.quit()

