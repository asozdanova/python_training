
from model.group import Group
from random import randrange

def test_delete_some_group(app):
    if app.group.count() ==0:
        app.group.init_group_creation()
        app.group.fill_group_form(Group(name="test"))
        app.group.submit_group_creation()
    old_groups = app.group.get_group_list()
    index = randrange (len(old_groups))#индекс удаляемой группы
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count() #проверка длины, метод count выступает в роли хеша
    new_groups = app.group.get_group_list()
    old_groups[index:index+1]=[]
    assert old_groups == new_groups