import re
from playwright.sync_api import Page


def test_has_title(page: Page):

    input_search_text =  "combobox"
    selectDocumentationforPythonOption = "playwright documentation python"

    page.goto("https://www.google.com/")
    page.wait_for_timeout(2000)
    page.frame_locator("iframe[name=\"callout\"]").get_by_label("Stay signed out").click()
    
    page.get_by_role(input_search_text).fill("playwright documentation")
    page.get_by_text(selectDocumentationforPythonOption).click()
    page.get_by_role(input_search_text).press('Enter')
    page.wait_for_timeout(2000)

    
   

