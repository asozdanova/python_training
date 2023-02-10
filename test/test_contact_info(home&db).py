from model.contact import Contact
import re

def test_contact_info(app,db):
    home_contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    db_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(home_contacts) == len(db_contacts)
    for index in range(len(db_contacts)):
        assert home_contacts[index].firstname == db_contacts[index].firstname
        assert home_contacts[index].lastname == db_contacts[index].lastname
        assert home_contacts[index].address == db_contacts[index].address
        assert home_contacts[index].email== merge_email_like_on_home_page(db_contacts[index])
        assert home_contacts[index].all_phones_from_home_page == merge_phones_like_on_home_page(db_contacts[index])

def clear(string):
    return re.sub('[() /*-]', '', string)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.phonehome,contact.phonemobile,contact.phonework,contact.phone2]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                                           [contact.email,contact.email2,contact.email3])))

