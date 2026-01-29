#Page Object Model(Login Page)

from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_btn = (By.CSS_SELECTOR, "button[type='submit']")
    message= (By.ID, "flash")
    def enter_username(self, user):
        self.driver.find_element(*self.username).send_keys(user)
    def enter_password(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)
    def click_login_btn(self):
        self.driver.find_element(*self.login_btn).click()
    def get_message(self):
        return self.driver.find_element(*self.message).text


#here i kept the locators seperate
#main purpose is easy maintenance
#industry standard POM