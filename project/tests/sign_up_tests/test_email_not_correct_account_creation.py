from tests.pages import locators
from webdriver_factory import WebDriverFactory
from tests.pages.main_page import MainPage

not_valid_email = 'Test'


class TestSignUp():
    driver = WebDriverFactory.get_driver('chrome')
    main_page = MainPage(driver)

    def test_setup(self):
        self.main_page.open_main_page()
        self.main_page.open_login_page()

    def test_email_field_validation(self):
        #  Enter the Not valid email value into the 'Email address' input box at the Registration area.
        self.driver.find_element_by_xpath(locators.EMAIL_FOR_REG_INPUT_BOX).send_keys('not_valid_email')
        # Click "Create an account" button to open the Sig Up form
        self.driver.find_element_by_xpath(locators.CREATE_ACCOUNT_BUTTON).click()
        # Verify that validation error appears
        assert self.driver.find_element_by_xpath(locators.VALIDATION_ERROR_EMAIL_CREATE).is_displayed(), \
            "The validation error doesn't appear"

    def test_teardown(self):
        self.driver.quit()
