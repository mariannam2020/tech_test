from tests.pages import locators
from webdriver_factory import WebDriverFactory
from tests.pages.main_page import MainPage


email_reg_value = 'qatest@mailinator.com'
password_value = 'TestQa'


class TestSignUpForm():
    driver = WebDriverFactory.get_driver('chrome')
    main_page = MainPage(driver)

    def test_setup(self):
        self.main_page.open_main_page()
        self.main_page.open_login_page()
        self.main_page.open_registration_form(email_reg_value)

    def test_registration_new_account(self):
        # Enter values at the form
        self.driver.find_element_by_xpath(locators.EMAIL_ADDRESS).send_keys(email_reg_value)
        self.driver.find_element_by_xpath(locators.PASSWORD).send_keys(password_value)
        self.driver.find_element_by_xpath(locators.CONFIRM_PASSWORD).send_keys(password_value)
        self.driver.find_element_by_xpath(locators.CHECKBOX_CIVIL_MISS).click()
        self.driver.find_element_by_xpath(locators.LAST_NAME).send_keys('Sandy')
        self.driver.find_element_by_xpath(locators.FIRST_NAME).send_keys('Katrin')
        self.driver.find_element_by_xpath(locators.BIRTH_DAY).send_keys('11')
        self.driver.find_element_by_xpath(locators.BIRTH_MONTH).send_keys('10')
        self.driver.find_element_by_xpath(locators.BIRTH_YEAR).send_keys('1985')
        self.driver.find_element_by_xpath(locators.STREET).send_keys('1234 Avenue de Rode')
        self.driver.find_element_by_xpath(locators.APPT).send_keys('Appartment 123')
        self.driver.find_element_by_xpath(locators.RESIDENCE).send_keys('Batiment li')
        # Zip Code Miami - 33111
        self.driver.find_element_by_xpath(locators.ZIP_CODE).send_keys('33111')

        # Verify that after the ZIP Code entered - the City value auto filled
        city_value = self.driver.find_element_by_xpath(locators.CITY)
        assert city_value == "Miami", "The city not correct"

        self.driver.find_element_by_xpath(locators.STATE).send_keys('Florida')
        self.driver.find_element_by_xpath(locators.MOBILE_PHONE).send_keys(email_reg_value)
        self.driver.find_element_by_xpath(locators.HOME_PHONE).send_keys(email_reg_value)
        self.driver.find_element_by_xpath(locators.CHECKBOX_NEWSLETTER).click()
        self.driver.find_element_by_xpath(locators.CONTINUE_BUTTON).click()
        # assert that registration performed successfully

    def test_teardown(self):
        self.driver.quit()
