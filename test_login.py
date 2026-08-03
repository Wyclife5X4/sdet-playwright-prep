from playwright.sync_api import expect

def test_successful_login(login_page):
    login_page.login("student", "Password123")

    expect(login_page.page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
    expect(login_page.page.get_by_role("heading", name="Logged In Successfully")).to_be_visible()

def test_invalid_password_login(login_page):
    login_page.login("student", "WrongPassword123")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("Your password is invalid!")
