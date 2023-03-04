import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Signin():
    def __init__(self, driver):
        self.driver = driver
        self.Signin_link_text = "SIGN-ON"
        self.Signin_username = "userName"
        self.Signin_password = "password"
        self.signin_submit_button_name = "submit"

    def Click_signin(self):
        self.driver.find_element(By.LINK_TEXT, "SIGN-ON").click()

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.Signin_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.Signin_password).send_keys(password)

    def signin_submit(self):
        self.driver.find_element(By.NAME, self.signin_submit_button_name).submit()
