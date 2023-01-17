from model.group import Group

def test_modify_group_first(app):
    if app.group.count() == 0:
        app.group.init_group_creation()
        app.group.fill_group_form(Group(name="test"))
        app.group.submit_group_creation()
    old_groups = app.group.get_group_list()
    app.group.modify_group_first(Group(name="newname",header="newheader", footer="newfooter"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)