
from model.group import Group
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        # return to groups page
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_xpath("//*/text()[normalize-space(.)='']/parent::*").click()
        wd.find_element_by_xpath("//form[@action='/addressbook/addressbook/group.php']").click()

    def submit_group_creation(self):
        wd = self.app.wd
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None #сброс кеша после создания группы

    def fill_group_form(self, group):
        wd = self.app.wd
        # fill group firm
        self.change_field_value("group_name",  group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, field_value):
        # значение поля будет меняться или оставаться таким каким было
        wd = self.app.wd
        if field_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_value)

    def init_group_creation(self):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)
    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        #select group
        self.select_group_by_index(index)
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None  # сброс кеша после удаления группы

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        #select group
        self.select_group_by_id(id)
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None  # сброс кеша после удаления группы
    def modify_group_first(self,group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # edit group
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None  # сброс кеша после модификации группы

    def select_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
    def select_group_by_index(self, index):
        wd = self.app.wd
        # select  group
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        # select  group
        wd.find_element_by_css_selector("input[value='%s']" % id).click()#кликаем по чекбоксу с заданным значением атрибута value

    def modify_group(self):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_param):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_param)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None  # сброс кеша после модификации группы

    def modify_group_by_id(self, id, new_group_param):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_param)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None  # сброс кеша после модификации группы

    def open_groups_page(self):
        # open groups page
        wd = self.app.wd
        #кол-во элементов, найденных по имени new >0 на странице group.php
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))>0):
             wd.find_element_by_link_text("groups").click()

    def count(self):
        #расчет кол-ва групп
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
           wd = self.app.wd
           self.open_groups_page()
           self.group_cache = []
           #запрос на получение нужных элементов на странице group
           for element in wd.find_elements_by_css_selector("span.group"):
               text = element.text
               #находим чекбокс внутри элемента span, у чекбокса атрибут value, это будет индентивикатор
               id = element.find_element_by_name("selected[]").get_attribute("value")
               self.group_cache.append(Group(name=text, id=id))
        #возвращение списка groups
        return list(self.group_cache) #возврат копии кеша



