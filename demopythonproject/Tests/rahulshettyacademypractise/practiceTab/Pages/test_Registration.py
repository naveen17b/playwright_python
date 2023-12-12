import re
from playwright.sync_api import Page
from PageObjects.Constants import LoginPageConstants

def test_Registration(page:Page):
    
    #browser = p.chromium.launch(headless=False)
    #page = browser.new_page()
    page = LoginPageConstants(page)
    page.navigate()
    page.nameTextbox("krishna")
    page.emailTextBox('seleniumpractice78@gmail.com')
    page.checkBox()
    page.SubmitButton()
    page.wait_for_time_out(3000)
    page.close()


   