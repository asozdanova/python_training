from model.contact import Contact

def test_modify_contact_first(app):
    app.session.login( username= "admin", password="secret")
    app.contact.modify_contact_first(Contact (firstname="petrov", middlename="petr", lastname="petr", address="address", phonehome="hometel", phonemobile="mobiletel", phonework="worktel", phonefax="faxtel",
                                         email= "mail", bday="7", bmonth="January", byear="1982"))
    app.session.logout()