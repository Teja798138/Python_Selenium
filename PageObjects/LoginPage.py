from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from Utilities.readproperties import ReadConfig


class LoginPage(BasePage):
    Email_textbox_id = (By.ID, "email")
    Password_textbox_id = (By.ID, "password")
    login_button = (By.XPATH, "//*[@id='loginButton']")
    branch = (By.XPATH, "//input[@id='btn_submit']")

    def login_check(self):
        self.enter_text(self.Email_textbox_id, ReadConfig.getUseremail())
        self.enter_text(self.Password_textbox_id, ReadConfig.getPassword())
        self.click(self.login_button)
        self.click(self.branch)

    def login_validations(self, username, password):
        self.enter_text(self.Email_textbox_id, username)
        self.enter_text(self.Password_textbox_id, password)
        self.click(self.login_button)




