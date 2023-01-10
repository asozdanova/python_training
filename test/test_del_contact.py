from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="alla", middlename="alla", lastname="sozdanova", address="address", phonehome="555",
                    phonemobile="999", phonework="777", phonefax="888", email="mail", bday="16", bmonth="July", byear="1982"))
    app.contact.delete_first_contact()