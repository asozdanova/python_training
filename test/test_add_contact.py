
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) #генератор случайных строк

testdata = [Contact(firstname="", middlename="", lastname="", address="", phonehome="", phonemobile="",
                    phonework="", phonefax="",email="", email2="", email3="")] + [
            Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                    lastname=random_string("lastname", 10),address=random_string("address", 10),
                    phonehome=random_string("phonehome", 10),phonemobile=random_string("address", 10),
                    phonework=random_string("phonework", 10), phonefax=random_string("phonefax", 10),
                    email=random_string("email", 10),email2=random_string("email2", 10), email3=random_string("email3", 10))
            for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app,contact):
    old_contacts = app.contact.get_contact_list() #сохранить старый список контактов
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count() #проверка длины, метод count выступает в роли хеша
    new_contacts = app.contact.get_contact_list()  # новый список контактов
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)  # сравнение отсортированных контактов


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()  # сохранить старый список контактов
#    contact = Contact (firstname="", middlename="", lastname="", address="", phonehome="", phonemobile="", phonework="", phonefax="",email="")
#    app.contact.create_contact(contact)
#    new_contacts = app.contact.get_contact_list()  # новый список контактов
#    assert len(old_contacts) + 1 == len(new_contacts)  # сравнение старых и новых контактов
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)  # сравнение отсортированных контактов




