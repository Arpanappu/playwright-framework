from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://the-internet.herokuapp.com/download")

    with page.expect_download() as download_info:
        page.click("text=some-file.txt")

    download = download_info.value
    download.save_as("downloaded_file.txt")

    browser.close()