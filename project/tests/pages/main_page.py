from tests.pages import locators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://marksandspicy.com/")
        return self

    def open_login_page(self):
        self.driver.find_element_by_xpath(locators.LOGIN_LINK).click()
        # Verify that needed page is opened
        assert self.driver.find_element_by_xpath(locators.LOGIN_PAGE_IDENTIFICATION), "The Login page isn't opened"
        return self

    def open_registration_form(self, email_reg_value):
        #  Enter the email value into the 'Email address' input box at the Registration area.
        self.driver.find_element_by_xpath(locators.EMAIL_FOR_REG_INPUT_BOX).send_keys(email_reg_value)
        # Click "Create an account" button to open the Sig Up form
        self.driver.find_element_by_xpath(locators.CREATE_ACCOUNT_BUTTON).click()
        # Verify that the form opened
        page_title = self.driver.title
        assert page_title == "Sign Up", "The Registration form doesn't open"
        return self
