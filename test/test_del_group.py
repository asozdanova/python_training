
from model.group import Group
import random

def test_delete_some_group(app,db):
    if len(db.get_group_list())==0:#обращение к бд
        app.group.init_group_creation()
        app.group.fill_group_form(Group(name="test"))
        app.group.submit_group_creation()
    old_groups = db.get_group_list()#получение списков
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups) #проверка длины, метод count выступает в роли хеша
    old_groups.remove(group)#удаляется выбранный элемент
    assert old_groups == new_groups