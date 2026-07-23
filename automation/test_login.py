from playwright.sync_api import sync_playwright

BASE_URL = "https://www.saucedemo.com"


def test_successful_login(page):
    """Тест-кейс #4: успешный вход с валидными данными"""
    page.goto(BASE_URL)
    page.fill('[data-test="username"]', 'standard_user')
    page.fill('[data-test="password"]', 'secret_sauce')
    page.click('[data-test="login-button"]')
    assert "inventory.html" in page.url


def test_empty_fields_login(page):
    """Тест-кейс #1: вход с пустыми полями"""
    page.goto(BASE_URL)
    page.fill('[data-test="username"]', '')
    page.fill('[data-test="password"]', '')
    page.click('[data-test="login-button"]')
    assert page.is_visible("text=Epic sadface: Username is required")


def test_locked_out_user_login(page):
    """Тест-кейс #5: вход заблокированным пользователем"""
    page.goto(BASE_URL)
    page.fill('[data-test="username"]', 'locked_out_user')
    page.fill('[data-test="password"]', 'secret_sauce')
    page.click('[data-test="login-button"]')
    assert page.is_visible("text=Epic sadface: Sorry, this user has been locked out.")


def test_invalid_credentials_login(page):
    """Тест-кейс #3: вход с неверными данными"""
    page.goto(BASE_URL)
    page.fill('[data-test="username"]', 'wrong_user')
    page.fill('[data-test="password"]', 'wrong_pass')
    page.click('[data-test="login-button"]')
    assert page.is_visible(
        "text=Epic sadface: Username and password do not match any user in this service"
    )
