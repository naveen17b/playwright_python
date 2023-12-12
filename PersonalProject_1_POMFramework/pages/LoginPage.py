
"""   This Login Page has all the locators and credentials of the Login Page    """
from PersonalProject_1_POMFramework.pages.AddItemPage import AddItemPage


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.page = page.goto("https://www.saucedemo.com/")
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login = page.locator("input#login-button")

    def user_name(self, u_name):
        self.enter_username.fill(u_name)

    def pass_word(self, p_word):
        self.enter_password.fill(p_word)

    def login_button(self):
        self.login.click()

    def login_functionality(self, value):
        self.user_name(value['username'])
        self.pass_word(value['password'])
        self.login_button()
        return AddItemPage(self.page)


