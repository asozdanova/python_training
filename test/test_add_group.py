
from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) #генератор случайных строк



testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20),
          footer=random_string("footer", 20))
    for i in range(5)
]
@pytest.mark.parametrize("group",testdata,ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.init_group_creation()
    app.group.fill_group_form(group)
    app.group.submit_group_creation()
    assert len(old_groups) + 1 == app.group.count() #проверка длины, метод count выступает в роли хеша
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)  # сравнение отсортированных групп


#def test_add_empty_group(app):
#   old_groups = app.group.get_group_list()
#   app.group.init_group_creation()
#   group = Group(name="", header="", footer="")
#   app.group.fill_group_form(group)
#   app.group.submit_group_creation()
#   new_groups = app.group.get_group_list()
#   assert len(old_groups) + 1 == len(new_groups)
#   old_groups.append(group)
#   assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # сравнение отсортированных групп






