
from model.contact import Contact


def test_add_contact(app):
    app.contact.create_contact(Contact (firstname="ivanov", middlename="ivan", lastname="kkhhn", address="jnhtbhn", phonehome="kkjnh", phonemobile="kjnb", phonework="kjnhhy", phonefax="kjnhy",
                                         email= "as@mail.ru"))

def test_add_empty_contact(app):
    app.contact.create_contact(Contact (firstname="", middlename="", lastname="", address="",
                                         phonehome="", phonemobile="", phonework="", phonefax="",
                                         email=""))



