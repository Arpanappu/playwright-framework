from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://the-internet.herokuapp.com/upload")

    page.set_input_files("#file-upload", "onlykonnect.txt")

    page.click("#file-submit")

    page.screenshot(path="file_upload.png")

    browser.close()