from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False)
    
    page = browser.new_page()
    
    page.goto("https://www.google.com")
    
    page.fill("textarea[name='q']", "Playwright Python tutorial")
    
    page.keyboard.press("Enter")
    
    page.wait_for_timeout(15000)
    
    browser.close()