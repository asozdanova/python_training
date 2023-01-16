from model.contact import Contact

def test_modify_contact_first_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="alla", middlename="alla", lastname="sozdanova", address="address", phonehome="555",
                    phonemobile="999", phonework="777", phonefax="888", email="mail"))
    app.contact.modify_contact_first(Contact (firstname="petr"))

def test_modify_contact_first_lastname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="alla", middlename="alla", lastname="sozdanova", address="address", phonehome="555",
                    phonemobile="999", phonework="777", phonefax="888", email="mail"))
    app.contact.modify_contact_first(Contact (lastname="petrov"))