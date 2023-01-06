
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
    app.session.login( username="admin", password="secret")
    app.group.init_group_creation()
    app.group.fill_group_firm(Group(name="test2", header="nhflflf", footer="nhfflf"))
    app.group.submit_group_creation()
    app.session.logout()

def test_untitled_test_case_empty(app):
        # login
   app.session.login(username="admin", password="secret")
   app.group.init_group_creation()
   app.group.fill_group_firm(Group(name="", header="", footer=""))
   app.group.submit_group_creation()
   app.session.logout()






