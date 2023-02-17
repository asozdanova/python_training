from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.init_group_creation()
        app.group.fill_group_form(Group(name="test2", header="nhflflf", footer="nhfflf"))
        app.group.submit_group_creation()
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="1n", lastname="3n", address="Test address",
                                    phonehome="+09875444", phonemobile="+79897896756", phonework="+79897896356",
                                           phone2="+70008986756", email="t@test.com", email2="t@test2.com", email3="t@test3.com"))
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    contact0 = random.choice(old_contacts)
    group0 = random.choice(old_groups)
    old_list = db.get_contacts_in_group(group0.id)
    if len(db.get_contacts_in_group(group0.id)) == 0:
        app.contact.add_contact_to_group_by_id(contact0.id, group0.id)
    old_list = db.get_contacts_in_group(group0.id)
    contact0 = random.choice(old_list)
    app.contact.delete_contact_from_group_by_id(contact0.id, group0.id)
    old_list.remove(contact0)
    new_list = db.get_contacts_in_group(group0.id)
    assert old_list == new_list