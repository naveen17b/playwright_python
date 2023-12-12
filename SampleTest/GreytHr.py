import re
from playwright.sync_api import Page


def test_login(page: Page):

     page.goto("https://zelarsoftprivatelimited.greythr.com/")
     page.wait_for_timeout(5000)

