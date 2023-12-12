class LoginPageConstants:

    def __init__(self, page):
        self.page = page
        self._practiceTab = page.get_by_text("Practice")
        self._nameId = page.locator("input#name")
        self._email_Text_Box = page.get_by_placeholder("Your Email*")
        self.agree_Check_Box = page.locator("input#agreeTerms")
        self.click_Submit_Button = page.locator("form-submit")

    def navigate(self):
       self.page.goto("https://rahulshettyacademy.com/")

    def nametextbox(self, text):
        self._nameId.fill(text)

    def emailtextBox(self,text):
        self._email_Text_Box.fill(text)

    def checkbox(self):
        self.agree_Check_Box.click()

    def submitbutton(self,click):
        self.click_Submit_Button.click()        
        
             