
from model.contact import Contact


def test_add_contact(app):
    app.contact.create_contact(Contact (firstname="ivanov", middlename="ivan", lastname="kkhhn", address="jnhtbhn", phonehome="kkjnh", phonemobile="kjnb", phonework="kjnhhy", phonefax="kjnhy",
                                         email= "kjhyt", bday="16", bmonth="January", byear="1982"))

def test_add_empty_contact(app):
    app.contact.create_contact(Contact (firstname="", middlename="", lastname="", address="",
                                         phonehome="", phonemobile="", phonework="", phonefax="",
                                         email="", bday="", bmonth="-", byear=""))



