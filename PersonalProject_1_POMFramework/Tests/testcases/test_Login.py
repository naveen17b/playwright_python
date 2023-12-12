"""   This is a playwright test  to check the login functionality of the Example website  of Swag labs with the working
URl --> https://www.saucedemo.com/   """

from playwright.sync_api import Page, expect

"""  we have to maintain a space between import module """


def test_login_functionality(page: Page):

    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("input#login-button").click()
    page.wait_for_timeout(3000)
    title_of_page = page.title()
    print(f"Page Title: {title_of_page}")
    page.screenshot(path="screenshot.png")
    page.wait_for_timeout(3000)
    page.close()


def test_login_with_invalid_user(page: Page):

        page.goto("https://www.saucedemo.com/")
        page.get_by_placeholder("Username").fill("invalid_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.locator("input#login-button").click()
        page.wait_for_timeout(3000)

        error_message_text_content = "Username and password do not match any user in this service"
        error_message = "//h3[@data-test='error']"
        error_message_text = page.locator(error_message)

        print(error_message)
        expect(error_message_text).to_contain_text(error_message_text_content)
        page.screenshot(path="screenshot.png")
        page.wait_for_timeout(3000)
        page.close()


"""  command to run only this test block  ->  pytest -k test_login_invalid_password --headed  """


def test_login_invalid_password(page: Page):

    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret")
    page.locator("input#login-button").click()
    page.wait_for_timeout(3000)
    error_message_text_content = "Username and password do not match any user in this service"
    error_message = "//h3[@data-test='error']"
    error_message_text = page.locator(error_message)

    print(error_message)
    expect(error_message_text).to_contain_text(error_message_text_content)
    page.screenshot(path="screenshot.png")
    page.wait_for_timeout(3000)

    close_error_message = "button.error-button"
    page.locator(close_error_message).click()

    page.wait_for_timeout(3000)

    """ Login  with correct credentials """
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("input#login-button").click()
    page.wait_for_timeout(3000)

    page.locator("div.bm-burger-button").click()
    page.locator("a#logout_sidebar_link").click()
    page.screenshot(path="screenshot.png")
    page.wait_for_timeout(3000)
    page.close()

