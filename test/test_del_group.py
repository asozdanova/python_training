


def test_delete_first_group(app):
# login
    app.session.login( username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()