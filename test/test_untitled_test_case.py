
from model.group import Group

def test_untitled_test_case(app):
    app.group.init_group_creation()
    app.group.fill_group_form(Group(name="test2", header="nhflflf", footer="nhfflf"))
    app.group.submit_group_creation()

def test_untitled_test_case_empty(app):
   app.group.init_group_creation()
   app.group.fill_group_form(Group(name="", header="", footer=""))
   app.group.submit_group_creation()






