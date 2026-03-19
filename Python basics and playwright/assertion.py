from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.wikipedia.org")

    title = page.title()

    assert "Wikipedia" in title

    browser.close()