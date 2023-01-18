from model.contact import Contact

def test_modify_contact_first_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="alla", middlename="alla", lastname="sozdanova", address="address", phonehome="555",
                    phonemobile="999", phonework="777", phonefax="888", email="mail"))
    old_contacts = app.contact.get_contact_list()  # сохранить старый список контактов
    app.contact.modify_contact_first(Contact (firstname="petr"))
    new_contacts = app.contact.get_contact_list()  # новый список контактов
    assert len(old_contacts) == len(new_contacts)  # сравнение старых и новых контактов

def test_modify_contact_first_lastname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="alla", middlename="alla", lastname="sozdanova", address="address", phonehome="555",
                    phonemobile="999", phonework="777", phonefax="888", email="mail"))
    old_contacts = app.contact.get_contact_list()  # сохранить старый список контактов
    app.contact.modify_contact_first(Contact (lastname="petrov"))
    new_contacts = app.contact.get_contact_list()  # новый список контактов
    assert len(old_contacts) == len(new_contacts)  # сравнение старых и новых контактов
