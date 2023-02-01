from model.contact import Contact


#@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()  # сохранить старый список контактов
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()  # проверка длины, метод count выступает в роли хеша
    new_contacts = app.contact.get_contact_list()  # новый список контактов
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,
                                                                 key=Contact.id_or_max)  # сравнение отсортированных контактов

# def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()  # сохранить старый список контактов
#    contact = Contact (firstname="", middlename="", lastname="", address="", phonehome="", phonemobile="", phonework="", phonefax="",email="")
#    app.contact.create_contact(contact)
#    new_contacts = app.contact.get_contact_list()  # новый список контактов
#    assert len(old_contacts) + 1 == len(new_contacts)  # сравнение старых и новых контактов
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)  # сравнение отсортированных контактов
