import re
from playwright.sync_api import Page, expect


def test_successful_login(page: Page):
    # 1. Navigate to the practice login page
    page.goto("https://practicetestautomation.com/practice-test-login/")

    # 2. Fill in the Username using its label
    page.get_by_label("Username").fill("student")

    # 3. Fill in the Password using its label
    page.get_by_label("Password").fill("Password123")

    # 4. Click the Submit button
    page.get_by_role("button", name="Submit").click()

    # 5. Assert that we navigated to the success URL
    expect(page).to_have_url(
        "https://practicetestautomation.com/logged-in-successfully/"
    )

    # 6. Assert that the page displays the success heading
    expect(
        page.get_by_role("heading", name="Logged In Successfully")
    ).to_be_visible()

    print("\n✅ Successful login test passed!")


def test_invalid_password_login(page: Page):
    # 1. Navigate to login page
    page.goto("https://practicetestautomation.com/practice-test-login/")

    # 2. Fill in valid username but WRONG password
    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").fill("WrongPassword123")

    # 3. Click Submit
    page.get_by_role("button", name="Submit").click()

    # 4. Assert error message using locator("#error")
    error_message = page.locator("#error")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Your password is invalid!")

    print("\n✅ Invalid login test passed!")




    from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("student", "Password123")

    expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
    expect(page.get_by_role("heading", name="Logged In Successfully")).to_be_visible()

def test_invalid_password_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("student", "WrongPassword123")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("Your password is invalid!")