from tests.pages import locators
from webdriver_factory import WebDriverFactory
from tests.pages.main_page import MainPage

email = 'test'


class TestTooltip():
    driver = WebDriverFactory.get_driver('chrome')
    main_page = MainPage(driver)

    def test_setup(self):
        self.main_page.open_main_page()
        self.main_page.open_login_page()

    def test_username_tooltip(self):
        # Enter the email value not correct to the 'Email address' input box.
        self.driver.find_element_by_xpath(locators.EMAIL_INPUT_BOX).send_keys(email)
        # Click to the login form area to see the error
        self.driver.find_element_by_xpath(locators.LOGIN_FORM_AREA).click()

        # Verify that the email input box contain the attribute type - email;
        # browser according current type will show tooltip.
        email_field = self.driver.find_element_by_xpath(locators.EMAIL_INPUT_BOX)
        type_value = email_field.get_attribute("type")
        assert type_value == 'email', "The type doesn't contain value - email"

    def test_teardown(self):
        self.driver.quit()
