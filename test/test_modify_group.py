from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.init_group_creation()
        app.group.fill_group_form(Group(name="test"))
        app.group.submit_group_creation()
    old_groups = app.group.get_group_list()
    app.group.modify_group(Group(name="New name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.init_group_creation()
        app.group.fill_group_form(Group(name="test"))
        app.group.submit_group_creation()
    old_groups = app.group.get_group_list()
    app.group.modify_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
