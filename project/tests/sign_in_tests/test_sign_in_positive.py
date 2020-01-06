from tests.pages import locators
from webdriver_factory import WebDriverFactory
from tests.pages.main_page import MainPage

# need to provide existing account
email_value = 'qatest@mailinator.com'
passw_value = 'TestQa'


class TestLoginPositive():
    driver = WebDriverFactory.get_driver('chrome')
    main_page = MainPage(driver)

    def test_setup(self):
        self.main_page.open_main_page()
        self.main_page.open_login_page()

    def test_login(self):
        # Enter the email value into the 'Email address' input box.
        self.driver.find_element_by_xpath(locators.EMAIL_INPUT_BOX).send_keys(email_value)
        # Enter the password value into the 'Password' input box.
        self.driver.find_element_by_xpath(locators.PASSW_INPUT_BOX).send_keys(passw_value)
        self.driver.find_element_by_xpath(locators.SIGN_IN_BUTTON).click()
        # assert if login performed successfully

    def test_teardown(self):
        self.driver.quit()
