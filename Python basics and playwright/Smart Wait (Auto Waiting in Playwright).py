from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com")

    page.wait_for_selector("#user-name")

    page.fill("#user-name", "standard_user")

    page.wait_for_timeout(5000)

    browser.close()