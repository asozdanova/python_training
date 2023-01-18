
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list() #сохранить старый список контактов
    app.contact.create_contact(Contact (firstname="ivanov", middlename="ivan", lastname="kkhhn", address="jnhtbhn", phonehome="kkjnh", phonemobile="kjnb", phonework="kjnhhy", phonefax="kjnhy",
                                         email= "as@mail.ru"))
    new_contacts = app.contact.get_contact_list() #новый список контактов
    assert len(old_contacts) + 1 == len(new_contacts)# сравнение старых и новых контактов
def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()  # сохранить старый список контактов
    app.contact.create_contact(Contact (firstname="", middlename="", lastname="", address="",
                                         phonehome="", phonemobile="", phonework="", phonefax="",
                                         email=""))
    new_contacts = app.contact.get_contact_list()  # новый список контактов
    assert len(old_contacts) + 1 == len(new_contacts)  # сравнение старых и новых контактов



