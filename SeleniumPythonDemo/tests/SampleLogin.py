from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import unittest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.MercuryRegistration import Register_pages
from Pages.MercurySignin import Signin
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))



# driver = webdriver.Chrome(ChromeDriverManager().install()) used for selenium 3
# driver = webdriver.Chrome('chromedriver.exe') used for selenium 3
class WebAutomation(unittest.TestCase):
      @classmethod
      def setUpClass(cls):
         cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

         cls.driver.get("https://demo.guru99.com/test/newtours/")
         cls.driver.maximize_window()



      def testregister(self):


          driver = self.driver
          registerpage = Register_pages(driver)
          registerpage.click_Register()
          registerpage.enter_Firstname("lakshmi")
          registerpage.enter_lastname("balaga")
          registerpage.enter_phone("898989898")
          registerpage.enter_username("abc@gmail.com")
          registerpage.enter_address("hyderabad")
          registerpage.enter_city("Hyderabad Urban")
          registerpage.enter_state("Telangana")
          registerpage.enter_postalcode("56565656")
          registerpage.enter_country("INDIA")
          registerpage.enter_email("lakshmi@jaga.com")
          registerpage.enter_password("123456")
          registerpage.enter_confirm_password("123456")
          registerpage.submit_registration()




          """"
           self.driver.find_element(By.LINK_TEXT, "REGISTER").click()
          #self.driver.find_element(By.NAME, "firstName").send_keys("lakshmi")
          self.driver.find_element(By.NAME, "lastName").send_keys("balaga")
          self.driver.find_element(By.NAME, "phone").send_keys("999999999")
          self.driver.find_element(By.ID, "userName").send_keys("abc@gmail.com")
          self.driver.find_element(By.NAME, "address1").send_keys("hyderabad")
          self.driver.find_element(By.NAME, "city").send_keys("Hyderabad urban ")
          self.driver.find_element(By.NAME, "state").send_keys("Telanagana")
          self.driver.find_element(By.NAME, "postalCode").send_keys("56719010")
          time.sleep(5)
          self.select = Select(self.driver.find_element(By.NAME, "country"))
          self.select.select_by_visible_text("INDIA")
          self.driver.find_element(By.NAME, "email").send_keys("lakshmi@jag.com")
          self.driver.find_element(By.NAME, "password").send_keys("123456")
          self.driver.find_element(By.NAME, "confirmPassword").send_keys("123456")
          self.driver.find_element(By.NAME, "submit").submit()
          """

      def testsignin(self):
          driver= self.driver
          signin=Signin(driver)
          signin.Click_signin()
          signin.enter_username("abc@gmail.com")
          signin.enter_password("123456")
          signin.signin_submit()
          """
          self.driver.find_element(By.LINK_TEXT, "SIGN-ON").click()
          self.driver.find_element(By.NAME, "userName").send_keys("abc@gmail.com")
          self.driver.find_element(By.NAME, "password").send_keys("123456")
          self.driver.find_element(By.NAME, "submit").submit()
          """
      @classmethod
      def tearDownClass(cls):
          cls.driver.close()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/jagad/PycharmProjects/SeleniumPythonDemo/reports'))







# from webdriver_manager.chrome import ChromeDriverManager













