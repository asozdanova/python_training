from model.contact import Contact
from random import randrange
def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="alla", middlename="alla", lastname="sozdanova", address="address", phonehome="555",
                    phonemobile="999", phonework="777", phonefax="888", email="mail"))
    old_contacts = app.contact.get_contact_list()  # сохранить старый список контактов
    index = randrange(len(old_contacts))  # индекс модифицируемого контакта
    contact = Contact (firstname="petr", middlename="PETR", lastname="ivanov", address="address2", phonehome="667",
                        phonemobile="3536")
    contact.id = old_contacts[index].id  # запоминаем идентификатор контакта
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count() #проверка длины, метод count выступает в роли хеша
    new_contacts = app.contact.get_contact_list()  # новый список контактов
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_contact_first_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create_contact(Contact(firstname="alla", middlename="alla", lastname="sozdanova", address="address", phonehome="555",
#                    phonemobile="999", phonework="777", phonefax="888", email="mail"))
#    old_contacts = app.contact.get_contact_list()  # сохранить старый список контактов
#    app.contact.modify_contact_first(Contact (lastname="petrov"))
#    new_contacts = app.contact.get_contact_list()  # новый список контактов
#    assert len(old_contacts) == len(new_contacts)  # сравнение старых и новых контактов
