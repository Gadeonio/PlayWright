from playwright.sync_api import sync_playwright
if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        page.goto("https://playwright.dev/")
        page.screenshot(path="example.png")
        browser.close()