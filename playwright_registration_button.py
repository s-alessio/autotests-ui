from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Open non-headless Chromium
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()  # Create new page


    # Open https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
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

    # Verify that registration button is disabled
    expect(reg_button).to_be_disabled()

    # Fill in input fields

    email_input.focus()
    for c in "user.name@gmail.com":
        page.keyboard.type(c)

    username_input.focus()
    for c in "username":
        page.keyboard.type(c)

    password_input.focus()
    for c in "password":
        page.keyboard.type(c)

    # Verify that registration button is enabled
    expect(reg_button).to_be_enabled()

