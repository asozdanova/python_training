from model.contact import Contact

def test_modify_contact_first_firstname(app):
    app.contact.modify_contact_first(Contact (firstname="petr"))

def test_modify_contact_first_lastname(app):
    app.contact.modify_contact_first(Contact (lastname="petrov"))