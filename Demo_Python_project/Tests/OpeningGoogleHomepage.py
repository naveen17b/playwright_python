import re
from playwright.sync_api import Page

def test_has_title(page: Page):
    page.goto("https://www.google.com/")
    page.wait_for_timeout(2000)

    input_search_text =  "combobox"
    
    page.get_by_role(input_search_text).fill("playwright documentation")
    page.get_by_role(input_search_text).press('Enter')
    page.wait_for_timeout(2000)

    
   

