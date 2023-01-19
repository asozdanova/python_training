from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="alla", middlename="alla", lastname="sozdanova", address="address", phonehome="555",
                    phonemobile="999", phonework="777", phonefax="888", email="mail"))
    old_contacts = app.contact.get_contact_list()  # сохранить старый список контактов
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count() #проверка длины, метод count выступает в роли хеша
    new_contacts = app.contact.get_contact_list()  # новый список контактов
    old_contacts[0:1] = []
    assert old_contacts == new_contacts