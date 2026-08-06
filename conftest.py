import os
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page: Page):
    """
    Fixture to initialize LoginPage and navigate to the login page 
    automatically before each test function runs.
    """
    login_obj = LoginPage(page)
    login_obj.navigate()
    return login_obj

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture a screenshot automatically on test failure.
    """
    outcome = yield
    report = outcome.get_result()

    # Check if the test step failed during execution
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if not page and "login_page" in item.funcargs:
            page = item.funcargs["login_page"].page

        if page:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"\n📸 Failure screenshot saved to: {screenshot_path}")
