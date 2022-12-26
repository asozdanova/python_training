
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
    
    def test_untitled_test_case(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/addressbook/")
        wd.find_element_by_xpath("//div[@id='footer']/ul/li").click()
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.get("https://software-testing.ru/lms/mod/page/view.php?id=290514")
        wd.find_element_by_id("yui_3_17_2_1_1672065391446_105").click()
        wd.find_element_by_xpath("//div[@id='yui_3_17_2_1_1672065391446_107']/div[5]/div/div[2]").click()
        wd.find_element_by_id("yui_3_17_2_1_1672065391446_105").click()
        wd.find_element_by_id("yui_3_17_2_1_1672065391446_105").click()
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        wd.get("http://localhost/addressbook/addressbook/")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_id("container").click()
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        wd.get("https://software-testing.ru/lms/mod/page/view.php?id=290514")
        wd.find_element_by_id("yui_3_17_2_1_1672065391446_105").click()
        wd.find_element_by_id("yui_3_17_2_1_1672065391446_105").click()
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        wd.get("http://localhost/addressbook/addressbook/")
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        wd.get("https://software-testing.ru/lms/mod/page/view.php?id=290514")
        wd.find_element_by_id("yui_3_17_2_1_1672065391446_105").click()
        wd.find_element_by_id("yui_3_17_2_1_1672065391446_105").click()
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        wd.get("http://localhost/addressbook/addressbook/group.php?new=New+group")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("test")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("jkkl")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("jkkl")
        wd.find_element_by_xpath("//form[@action='/addressbook/addressbook/group.php']").click()
        wd.find_element_by_name("submit").click()
        wd.get("http://localhost/addressbook/addressbook/group.php")
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        wd.get("https://software-testing.ru/lms/mod/page/view.php?id=290514")
        wd.find_element_by_id("yui_3_17_2_1_1672065391446_105").click()
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        wd.get("http://localhost/addressbook/addressbook/group.php")
        wd.find_element_by_link_text("groups").click()
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        #ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("test2")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("nhflflf")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("nhfflf")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_xpath("//*/text()[normalize-space(.)='']/parent::*").click()
        wd.find_element_by_xpath("//form[@action='/addressbook/addressbook/group.php']").click()
        wd.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    
    def tearDown(self):
        self.wd.quit()
