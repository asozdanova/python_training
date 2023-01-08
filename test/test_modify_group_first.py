from model.group import Group

def test_modify_group_first(app):
# login
    app.group.modify_group_first(Group(name="newname",header="newheader", footer="newfooter"))