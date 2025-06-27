import pytest
from playwright.sync_api import expect
from playwright.sync_api import Playwright, Page

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()  # Create new page

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Registration form elements
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    reg_button = page.get_by_test_id("registration-page-registration-button")

    expect(email_input).to_be_visible()
    expect(username_input).to_be_visible()
    expect(password_input).to_be_visible()
    expect(reg_button).to_be_visible()

    # Fill in and submit registration form
    email_input.fill("user.name@gmail.com")
    username_input.fill("username")
    password_input.fill("password")
    reg_button.click()

    context.storage_state(path="./files/browser-state.json")


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    # Реализация логики работы фикстуры
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="./files/browser-state.json")
    yield context.new_page()
    browser.close()