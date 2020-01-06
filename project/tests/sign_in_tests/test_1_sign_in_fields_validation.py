from tests.pages import locators
from webdriver_factory import WebDriverFactory
from tests.pages.main_page import MainPage


email_value = 'testtest.com'
passw_value = 'ThisIs@T3st'


class TestLogin():
    driver = WebDriverFactory.get_driver('chrome')
    main_page = MainPage(driver)

    def test_setup(self):
        self.main_page.open_main_page()
        self.main_page.open_login_page()

    def test_login(self):
        # Enter the email value not correct - without @ to the 'Email address' input box.
        self.driver.find_element_by_xpath(locators.EMAIL_INPUT_BOX).send_keys(email_value)
        # Enter the password value into the 'Password' input box.
        self.driver.find_element_by_xpath(locators.PASSW_INPUT_BOX).send_keys(passw_value)

        assert self.driver.find_element_by_xpath(
            locators.VALIDATION_ERROR_EMAIL).is_displayed(), \
            "The validation error doesn't appear"

    def test_teardown(self):
        self.driver.quit()
