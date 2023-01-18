
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list() #сохранить старый список контактов
    contact = Contact(firstname="ivanov", middlename="ivan", lastname="kkhhn", address="jnhtbhn", phonehome="kkjnh", phonemobile="kjnb", phonework="kjnhhy", phonefax="kjnhy",
                                         email= "as@mail.ru")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list() #новый список контактов
    assert len(old_contacts) + 1 == len(new_contacts)# сравнение старых и новых контактов
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)  # сравнение отсортированных контактов


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()  # сохранить старый список контактов
    contact = Contact (firstname="", middlename="", lastname="", address="", phonehome="", phonemobile="", phonework="", phonefax="",
                                         email="")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()  # новый список контактов
    assert len(old_contacts) + 1 == len(new_contacts)  # сравнение старых и новых контактов
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)  # сравнение отсортированных контактов




