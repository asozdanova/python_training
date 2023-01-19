from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="alla", middlename="alla", lastname="sozdanova", address="address", phonehome="555",
                    phonemobile="999", phonework="777", phonefax="888", email="mail"))
    old_contacts = app.contact.get_contact_list()  # сохранить старый список контактов
    index = randrange(len(old_contacts))  # индекс удаляемого контакта
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count() #проверка длины, метод count выступает в роли хеша
    new_contacts = app.contact.get_contact_list()  # новый список контактов
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts