from model.contact import Contact

def test_modify_contact_first(app):
    app.contact.modify_contact_first(Contact (firstname="petrov", middlename="petr", lastname="petr", address="address", phonehome="hometel", phonemobile="mobiletel", phonework="worktel", phonefax="faxtel",
                                         email= "mail"))