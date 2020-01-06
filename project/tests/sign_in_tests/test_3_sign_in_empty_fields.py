from tests.pages import locators
from webdriver_factory import WebDriverFactory
from tests.pages.main_page import MainPage


class TestEmptyFields():
    driver = WebDriverFactory.get_driver('chrome')
    main_page = MainPage(driver)

    def test_setup(self):
        self.main_page.open_main_page()
        self.main_page.open_login_page()

    def test_empty_fields_validation(self):
        # Click to the email input box, without enter any value
        self.driver.find_element_by_xpath(locators.EMAIL_INPUT_BOX).click()
        # Click to the password input box, without enter any value
        self.driver.find_element_by_xpath(locators.PASSW_INPUT_BOX).click()
        # Click to the login form area to see the error
        self.driver.find_element_by_xpath(locators.LOGIN_FORM_AREA).click()
        # Verify that the validation appears at the email input box
        assert self.driver.find_element_by_xpath(
            locators.VALIDATION_ERROR_EMAIL).is_displayed(), 'The validation doesn\'t appear for email input box'
        # Verify that the validation appears at the password input box
        assert self.driver.find_element_by_xpath(
            locators.VALIDATION_ERROR_PASSW).is_displayed(), 'The validation doesn\'t appear for password input box'

    def test_teardown(self):
        self.driver.quit()
