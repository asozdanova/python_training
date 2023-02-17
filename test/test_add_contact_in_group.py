from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

def test_add_contact_in_group(app,db,check_ui):
    #Если группы нет, то добавляем
    if len(db.get_group_list()) == 0:
        app.group.init_group_creation()
        app.group.fill_group_form(Group(name="test2", header="nhflflf", footer="nhfflf"))
        app.group.submit_group_creation()
    # Есть ли контакты
    if len(db.get_contact_list()) == 0:
       app.contact.create_contact(Contact(firstname="1n", lastname="3n", address="Test address",
                                    phonehome="+09875444", phonemobile="+79897896756", phonework="+79897896356",
                                           phone2="+70008986756", email="t@test.com", email2="t@test2.com", email3="t@test3.com"))
    list_groups = db.get_group_list()
    group0 = random.choice(list_groups)
    old_list = db.get_contacts_in_group(group0.id)
    add_list = db.get_contacts_not_in_group(group0.id)
    if len(add_list) == 0:
        app.contact.create_contact(Contact(firstname="1n", lastname="3n", address="Test address",
                                    phonehome="+09875444", phonemobile="+79897896756", phonework="+79897896356",
                                           phone2="+70008986756", email="t@test.com",email2="t@test2.com", email3="t@test3.com"))
        add_list = db.get_contacts_not_in_group(group0.id)
    contact0 = random.choice(add_list)
    app.contact.add_contact_to_group_by_id(contact0.id, group0.id)
    new_list = db.get_contacts_in_group(group0.id)
    old_list.append(contact0)
    assert sorted(old_list, key=Group.id_or_max) == sorted(new_list, key=Group.id_or_max)