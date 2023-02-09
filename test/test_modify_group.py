from model.group import Group
from random import randrange

def test_modify_group_name(app,db,check_ui):
    if len(db.get_group_list())==0:
        app.group.init_group_creation()
        app.group.fill_group_form(Group(name="test"))
        app.group.submit_group_creation()
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))  # индекс модифицируемой группы
    group = Group(name="New name")
    group.id = old_groups[index].id # запоминаем идентификатор группы
    app.group.modify_group_by_id(group.id,group)
    assert len(old_groups) == app.group.count() #проверка длины, метод count выступает в роли хеша
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:#если высставлен флаг check_ui
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),key=Group.id_or_max)# список из бд=список из ui


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#       app.group.init_group_creation()
#       app.group.fill_group_form(Group(name="test"))
#       app.group.submit_group_creation()
#    old_groups = app.group.get_group_list()
#    app.group.modify_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
