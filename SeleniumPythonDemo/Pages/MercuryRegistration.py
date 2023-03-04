import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Register_pages():
    def __init__(self, driver):
        self.driver = driver
        self.registration_linktext = "REGISTER"
        self.registration_firstname_txtbox_name = "firstName"
        self.registration_lastname_txtbox_name = "lastName"
        self.registration_phone_txtbox_name = "phone"
        self.registration_username_txtbox_id = "userName"
        self.registration_address_txtbox_name = "address1"
        self.registration_city_txtbox_name = "city"
        self.registration_state_txtbox_name = "state"
        self.registration_postalCode_txtbox_name = "postalCode"
        self.registration_country_txtbox_name = "country"
        self.registration_email_txtbox_name = "email"
        self.registration_password_txtbox_name = "password"
        self.registration_confirmpassword_txtbox_name = "confirmPassword"
        self.registration_submit_button_name = "submit"

    def click_Register(self):
        self.driver.find_element(By.LINK_TEXT, self.registration_linktext).click()

    def enter_Firstname(self, firstname):
        self.driver.find_element(By.NAME, self.registration_firstname_txtbox_name).clear()
        self.driver.find_element(By.NAME, self.registration_firstname_txtbox_name).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.NAME, self.registration_lastname_txtbox_name).send_keys(lastname)

    def enter_phone(self, phone):
        self.driver.find_element(By.NAME, self.registration_phone_txtbox_name).send_keys(phone)

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.registration_username_txtbox_id).send_keys(username)

    def enter_address(self, address):
        self.driver.find_element(By.NAME, self.registration_address_txtbox_name).send_keys(address)

    def enter_city(self, city):
        self.driver.find_element(By.NAME, self.registration_city_txtbox_name).send_keys(city)

    def enter_state(self, state):
        self.driver.find_element(By.NAME, self.registration_state_txtbox_name).send_keys(state)

    def enter_postalcode(self, postalcode):
        self.driver.find_element(By.NAME, self.registration_postalCode_txtbox_name).send_keys(postalcode)
        time.sleep(5)

    def enter_country(self, country):
        select = Select(self.driver.find_element(By.NAME, self.registration_country_txtbox_name))
        select.select_by_visible_text(country)

    def enter_email(self, email):
        self.driver.find_element(By.NAME, self.registration_email_txtbox_name).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.registration_password_txtbox_name).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.NAME, self.registration_confirmpassword_txtbox_name).send_keys(confirm_password)

    def submit_registration(self):
        self.driver.find_element(By.NAME, self.registration_submit_button_name).submit()


