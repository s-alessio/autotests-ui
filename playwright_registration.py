from playwright.sync_api import sync_playwright, expect  # Импорт Playwright для синхронного режима и проверки

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()  # Создаем новую страницу


    # Открываем страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Определяем элементы формы регистрации
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    reg_button = page.get_by_test_id("registration-page-registration-button")

    expect(email_input).to_be_visible()
    expect(username_input).to_be_visible()
    expect(password_input).to_be_visible()
    expect(reg_button).to_be_visible()

    # Заполнение и сабмит формы регистрации
    email_input.fill("user.name@gmail.com")
    username_input.fill("username")
    password_input.fill("password")
    reg_button.click()

    # Проверка того, что попали на нужную страницу
    dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text("Dashboard")

