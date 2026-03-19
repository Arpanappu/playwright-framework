from pages.login_page import LoginPage


def test_valid_login(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in page.url


def test_invalid_login(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "wrong_pass")
    assert "Epic sadface" in login.get_error()


def test_empty_login(page):
    login = LoginPage(page)
    login.open()
    login.login("", "")
    assert "Epic sadface" in login.get_error()


def test_password_empty_login(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "")
    assert "Epic sadface" in login.get_error()