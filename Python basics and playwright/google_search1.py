from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.google.com")

    page.fill("textarea[name='q']","Best crickt bat in india")

    page.keyboard.press("Enter")
    
    page.wait_for_timeout(18000)
    
    browser.close()