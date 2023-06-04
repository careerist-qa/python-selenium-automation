class Page:

    def __init__(self):
        self.base_url = 'https://www.amazon.com/'

    def click(self, some_locator):
        print('Clicking on smth')

    def text_input(self):
        print('Inputting text....')

class SignIn(Page):

    def click_login_btn(self):
        self.click('locator_for_login_btn')

    def login(self):
        self.click_login_btn()

    def open_signin(self):
        print(f"Opening {self.base_url+'signin'}")


class Registration(Page):

    def click_signup_btn(self):
        self.click('locator_for_signup_btn')


signin_page = SignIn()
# print(signin_page.base_url)
signin_page.open_signin()