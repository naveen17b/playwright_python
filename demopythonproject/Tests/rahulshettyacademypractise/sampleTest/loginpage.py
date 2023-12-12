import re
from playwright.sync_api import Page, expect

class loginTest:

    def test_Login_page(page: Page):

        loginButton = 'Login'
        emailTextBox = "input#email"
        passwordTextBox = "input#password"
        checkBoxLocator = "input[type='checkbox']"
        AuthunticationCheckBox = "input[type='checkbox']"

     # testconfig
        username = "automationpractice49@gmail.com"
        password = "Naveenb1794"

        page.goto("https://rahulshettyacademy.com/")
    # page.goto('https://sso.teachable.com/secure/9521/identity/login/password')
        page.get_by_text(loginButton).click()
        page.locator(AuthunticationCheckBox).click()
        page.get_by_test_id(emailTextBox).fill(username)
        page.get_by_test_id(passwordTextBox).fill(password)
        page.locator(checkBoxLocator).check()
        expect(checkBoxLocator).ischecked()
