from playwright.sync_api import sync_playwright

def handle_dialog(dialog):
    dialog.accept()

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.on("dialog", handle_dialog)


    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    
    page.click("text=Click for JS Alert")

    page.wait_for_timeout(5000)

    browser.close()