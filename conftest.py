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
