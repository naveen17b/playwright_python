import re
from playwright.sync_api import Page

# Create a Playwright instance
def test_playwright_sample(page:Page):

    page.goto("https://www.bing.com")
    # Print the page title
    print(page.title())

