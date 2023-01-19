from model.group import Group

def test_modify_group_first(app):
    if app.group.count() == 0:
        app.group.init_group_creation()
        app.group.fill_group_form(Group(name="test"))
        app.group.submit_group_creation()
    old_groups = app.group.get_group_list()
    group = Group(name="newname",header="newheader", footer="newfooter")
    group.id = old_groups[0].id  # запоминаем идентификатор группы
    app.group.modify_group_first(group)
    assert len(old_groups) == app.group.count() #проверка длины, метод count выступает в роли хеша
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
