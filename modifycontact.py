PK
     !�'V�d�!   !      requirements.txtselenium==3.141.0
urllib3==1.26.7PK
     !�'V               UntitledTestSuite/PK
     !�'V����	  �	  %   UntitledTestSuite/UntitledTestCase.py# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/addressbook/index.php")
        driver.find_element_by_id("10").click()
        driver.find_element_by_xpath("//table[@id='maintable']/tbody/tr[11]/td[8]/a/img").click()
        driver.get("http://localhost/addressbook/addressbook/edit.php?id=10")
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("ivanov2")
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("ivan2")
        driver.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        driver.get("http://localhost/addressbook/addressbook/edit.php")
        driver.find_element_by_link_text("home page").click()
        driver.get("http://localhost/addressbook/addressbook/index.php")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
PK 
     !�'V�d�!   !                    requirements.txtPK 
     !�'V                        O   UntitledTestSuite/PK 
     !�'V����	  �	  %                UntitledTestSuite/UntitledTestCase.pyPK      �   �
    