from model.contact import Contact
from random import randrange
import random

def test_delete_some_contact(app,db,check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="alla", middlename="alla", lastname="sozdanova", address="address", phonehome="555",
                    phonemobile="999", phonework="777", phonefax="888", email="mail"))
    old_contacts = db.get_contact_list()  # сохранить старый список контактов
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()  # новый список контактов
    assert len(old_contacts) - 1 == len(new_contacts) #проверка длины, метод count выступает в роли хеша
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
