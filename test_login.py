import pytest
from playwright.sync_api import expect

def test_successful_login(login_page):
    login_page.login("student", "Password123")

    expect(login_page.page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
    expect(login_page.success_message).to_be_visible()

@pytest.mark.parametrize("username, password, expected_error", [
    ("student", "WrongPassword123", "Your password is invalid!"),
    ("incorrectUser", "Password123", "Your username is invalid!"),
])
def test_invalid_login_scenarios(login_page, username, password, expected_error):
    login_page.login(username, password)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text(expected_error)
