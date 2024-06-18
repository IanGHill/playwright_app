from playwright.sync_api import sync_playwright

# test
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.google.com")
    page.screenshot(path="demo.png")
    browser.close()
