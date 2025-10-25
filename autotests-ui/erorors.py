from playwright.sync_api import sync_playwright, expect, Request, Response





with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    uncnown = page.locator('#uncnown')



    page.wait_for_timeout(5000)