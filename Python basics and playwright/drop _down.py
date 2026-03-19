from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://the-internet.herokuapp.com/dropdown")

    page.select_option("#dropdown", label="Option 2")

    page.wait_for_timeout(4000)

    browser.close()