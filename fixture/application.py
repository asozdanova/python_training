from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self,  browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get(self.base_url)

    def open_groups_page(self):
        # open groups page
        wd = self.wd
        # кол-во элементов, найденных по имени new >0 на странице group.php
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def destroy(self):
        self.wd.quit()
