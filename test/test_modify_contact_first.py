from model.contact import Contact

def test_modify_contact_first_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="alla", middlename="alla", lastname="sozdanova", address="address", phonehome="555",
                    phonemobile="999", phonework="777", phonefax="888", email="mail"))
    old_contacts = app.contact.get_contact_list()  # сохранить старый список контактов
    contact = Contact (firstname="petr")
    contact.id = old_contacts[0].id  # запоминаем идентификатор контакта
    app.contact.modify_contact_first(contact)
    new_contacts = app.contact.get_contact_list()  # новый список контактов
    assert len(old_contacts) == len(new_contacts)  # сравнение старых и новых контактов
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_contact_first_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create_contact(Contact(firstname="alla", middlename="alla", lastname="sozdanova", address="address", phonehome="555",
#                    phonemobile="999", phonework="777", phonefax="888", email="mail"))
#    old_contacts = app.contact.get_contact_list()  # сохранить старый список контактов
#    app.contact.modify_contact_first(Contact (lastname="petrov"))
#    new_contacts = app.contact.get_contact_list()  # новый список контактов
#    assert len(old_contacts) == len(new_contacts)  # сравнение старых и новых контактов
