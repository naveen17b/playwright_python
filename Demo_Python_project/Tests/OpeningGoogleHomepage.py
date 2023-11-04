import re
from playwright.sync_api import Page

def test_has_title(page: Page):
    page.goto("https://www.google.com/")
    page.wait_for_timeout(2000)

