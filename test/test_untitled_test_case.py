
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_untitled_test_case(app):
        # login
    app.login( username="admin", password="secret")
    app.init_group_creation()
    app.fill_group_firm(Group(name="test2", header="nhflflf", footer="nhfflf"))
    app.submit_group_creation()
    app.logout()

def test_untitled_test_case_empty(app):
        # login
   app.login(username="admin", password="secret")
   app.init_group_creation()
   app.fill_group_firm(Group(name="", header="", footer=""))
   app.submit_group_creation()
   app.logout()






