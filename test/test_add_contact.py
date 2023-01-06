
import pytest
from model.contact import Contact
from fixture.applicationcontact import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.open_home_page()
    app.login( username= "admin", password="secret")
    app.create_contact(Contact (firstname="ivanov", middlename="ivan", lastname="kkhhn", address="jnhtbhn", phonehome="kkjnh", phonemobile="kjnb", phonework="kjnhhy", phonefax="kjnhy",
                                         email= "kjhyt", bday="16", bmonth="January", byear="1982"))
    app.logout()

def test_add_empty_contact(app):
    app.open_home_page()
    app.login( username="admin", password="secret")
    app.create_contact(Contact (firstname="", middlename="", lastname="", address="",
                                         phonehome="", phonemobile="", phonework="", phonefax="",
                                         email="", bday="", bmonth="-", byear=""))
    app.logout()



