import re
from playwright.sync_api import Page, expect

def test_registration_page(page: Page):
    #constants
    SignUpLink='Sign Up'
    signUpButton ="Sign up with email"
    baseURL = "https://rahulshettyacademy.com/"
    titleOfPage = page.title() 
    registerButton = "Register"
    contactEmailTextLocator ='span.icon.fa.fa-envelope'
    clickOnContinueWithGoogleButton = "Continue with Google"
    userNameTextBox ="Email or phone"
    nextButton ="Next"
    passwordTextBox="Enter your password"
    

    #testconfig
    username ="automationpractice49@gmail.com"
    password = "Naveenb1794"

    #actual code
    page.goto(baseURL)
    page.wait_for_timeout(3000)
    print(titleOfPage)
    expect(page).to_have_url('https://rahulshettyacademy.com/')

    #registration of the user - click on register button
    #emailText = page.get_by_title(contactEmailTextLocator).text_content()
    #print(emailText)
    page.get_by_text(registerButton).click()
    #page.wait_for_timeout(5000)

    #login with google account
    page.get_by_text(clickOnContinueWithGoogleButton).click()
    page.wait_for_load_state('load')
    page.get_by_label(userNameTextBox).fill(username)
    page.get_by_text(nextButton).click()
    page.wait_for_timeout(3000)
    page.get_by_label(passwordTextBox).fill(password)
    page.get_by_text(nextButton).click()
    page.wait_for_timeout(5000)



    



    
