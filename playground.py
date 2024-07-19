
class Page:

    def click(self):
        print('Clicking...')

    def verify_text(self):
        print('Verifying...')

    def input_text(self, text):
        print(f'Inputting text, {text}')


class LoginPage(Page):
    def login(self):
        self.input_text('email')
        self.input_text('password')
        self.click()

class SignUpPage(Page):
    pass

login_page = LoginPage()
login_page.click()
login_page.login()
