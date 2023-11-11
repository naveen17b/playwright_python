import re
from playwright.sync_api import Page, expect

def test_registration_page(page: Page):
    #constants

    SignUpLink='Sign Up'
    signUpButton ="Sign up with email"
    baseURL = "https://rahulshettyacademy.com/"
    titleOfPage = page.title() 
    registerButton = "Register"
    fullNameTextBox = "Full Name"
    userNameTextBox = "Email"
    passwordTextBox = "input#password"
    SignUpSubmmitButton ="input[data-testid='signup-button']"

    #testconfig
    fullName='Naveen'
    username ="automationpractice49@gmail.com"
    password = "Naveenb1794"


  #actual code
    page.goto(baseURL)
    page.wait_for_timeout(3000)
    print(titleOfPage)
    expect(page).to_have_url('https://rahulshettyacademy.com/')

    page.get_by_text(registerButton).click()
    #page.get_by_alt_text(SignUpLink).click()
    page.get_by_text(signUpButton).click()
    page.wait_for_timeout(5000)
    page.get_by_text(fullNameTextBox).fill(fullName)
    page.get_by_text(userNameTextBox).fill(username)
    page.locator(passwordTextBox).fill(password)
    page.locator(SignUpSubmmitButton).click()
    page.wait_for_load_state('load')
    page.wait_for_timeout(10000)

    

