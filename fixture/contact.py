from selenium.webdriver.support.select import Select
from model.contact import Contact
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # open contact page
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_homepage()
        self.contact_cache = None  # сброс кеша после добавления контактов

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill contact firm and create contact
        self.change_field_value("firstname",contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.phonehome)
        self.change_field_value("work", contact.phonework)
        self.change_field_value("fax", contact.phonefax)
        self.change_field_value("email", contact.email)



    def change_field_value(self,field_name, field_value):
        #значение поля будет меняться или оставаться таким каким было
        wd = self.app.wd
        if field_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_value)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.open_home_page()
        # select  contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None  # сброс кеша после удаления контактов

    def modify_contact_first(self, new_contact_data):
        self.modify_contact_by_index(0)
    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        # select  contact
        wd.find_elements_by_name("selected[]")[index].click()
        # edit contact
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a").click()
        # fill contact firm
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_homepage()
        self.contact_cache = None  # сброс кеша после модификации контактов

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_link_text("Last name")) > 0):
            wd.find_element_by_link_text("home").click()

    def return_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        #подсчет кол-ва контактов
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
           wd = self.app.wd
           self.open_home_page()
           self.contact_cache = []
           # запрос на получение нужных элементов на странице
           for element in wd.find_elements_by_name('entry'):
               cells = element.find_elements_by_css_selector("td")
               lastname = cells[1].text
               firstname = cells[2].text
               # находим чекбокс внутри элемента, у чекбокса атрибут value, это будет индентивикатор
               id = element.find_element_by_name("selected[]").get_attribute("value")
               self.contact_cache.append(Contact(lastname = lastname, firstname=firstname, id=id))
        # возвращение списка contacts
        return list(self.contact_cache) #возврат копии кеша


