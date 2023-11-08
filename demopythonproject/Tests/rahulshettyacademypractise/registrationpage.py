import re
from playwright.sync_api import Page, expect

def Registration_page(page:Page):
    #constants
    baseURL = "https://rahulshettyacademy.com/"
    #titleOfPage = page.title()
    registerButton = "Register"
    contactEmailTextLocator ='span.icon.fa.fa-envelope'

    #actual code
    page.goto(baseURL)
    page.title()
    expect(page).to_have_url('https://rahulshettyacademy.com/')

    #registration of the user - click on register button
    emailText = page.get_by_title(contactEmailTextLocator).text_content()
    print (emailText)
    page.get_by_text(registerButton).click()
    



    
