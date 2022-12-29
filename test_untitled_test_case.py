
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_untitled_test_case(app):
        # login
    app.login(wd, username="admin", password="secret")
    app.init_group_creation(wd)
    app.fill_group_firm(wd, Group(name="test2", header="nhflflf", footer="nhfflf"))
    app.submit_group_creation(wd)
    app.logout(wd)

def test_untitled_test_case_empty(app):
        # login
   app.login(wd, username="admin", password="secret")
   app.init_group_creation(wd)
   app.fill_group_firm(wd, Group(name="", header="", footer=""))
   app.submit_group_creation(wd)
   app.logout(wd)






