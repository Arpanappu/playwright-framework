from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # open website
    page.goto("https://www.saucedemo.com")

    # Header screenshot
    page.locator(".login_logo").screenshot(path="header.png")

    # Login field screenshot
    page.locator("#user-name").screenshot(path="login_field.png")

    #Password Field
    page.locator("#password").screenshot(path="password_field.png")


    browser.close()