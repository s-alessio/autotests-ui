from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
        # Open non-headless Chromium
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()  # Create new page

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

        # Fill in and submit registration form
        email_input.fill("user.name@gmail.com")
        username_input.fill("username")
        password_input.fill("password")
        reg_button.click()

        context.storage_state(path="./files/browser-state.json")

    with sync_playwright() as playwright:
        # Open non-headless Chromium
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="./files/browser-state.json")
        page = context.new_page()  # Create new page

        # Open https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Verify elements of Courses page (this page can be shown to authorized user only)

        courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text("Courses")

        courses_list_icon = page.get_by_test_id("courses-list-empty-view-icon")
        expect(courses_list_icon).to_be_visible()

        courses_empty_list_title_text = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(courses_empty_list_title_text).to_be_visible()
        expect(courses_empty_list_title_text).to_have_text("There is no results")

        courses_empty_list_desc_text = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(courses_empty_list_desc_text).to_be_visible()
        expect(courses_empty_list_desc_text).to_have_text("Results from the load test pipeline will be displayed here")
