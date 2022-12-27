
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from group import Group

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path='C:\Python311\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
        self.wd.implicitly_wait(30)
    
    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        # login
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.init_group_creation(wd)
        self.fill_group_firm(wd, Group(name="test2", header="nhflflf", footer="nhfflf"))
        self.submit_group_creation(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_untitled_test_case_empty(self):
        wd = self.wd
        self.open_home_page(wd)
        # login
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.init_group_creation(wd)
        self.fill_group_firm(wd, Group(name="", header="", footer=""))
        self.submit_group_creation(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        # return to groups page
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_xpath("//*/text()[normalize-space(.)='']/parent::*").click()
        wd.find_element_by_xpath("//form[@action='/addressbook/addressbook/group.php']").click()

    def submit_group_creation(self, wd):
        # submit group creation
        wd.find_element_by_name("submit").click()

    def fill_group_firm(self, wd, group):
        # fill group firm
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def init_group_creation(self, wd):
        # init group creation
        wd.find_element_by_name("new").click()

    def open_groups_page(self, wd):
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()
        wd.find_element_by_xpath("//body").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/addressbook/")

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
