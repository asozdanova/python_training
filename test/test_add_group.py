
from model.group import Group

def test_add_group(app):
    app.group.init_group_creation()
    app.group.fill_group_form(Group(name="test2", header="nhflflf", footer="nhfflf"))
    app.group.submit_group_creation()

def test_add_empty_group(app):
   app.group.init_group_creation()
   app.group.fill_group_form(Group(name="", header="", footer=""))
   app.group.submit_group_creation()






