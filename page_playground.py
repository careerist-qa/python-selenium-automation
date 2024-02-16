
class BasePage:

    def open(self):
        print('Opening...')

    def click(self):
        print('Clicking')

    def verify_text(self):
        print('Verifying text...')

class LoginPage(BasePage):
    def login(self, username, pw):
        print(f'Logging in as {username}, {pw}...')

    def verify_text(self):
        print('Verifying LOGIN text...')

#
# page = BasePage()
# page.click()
# page.verify_text()

login_page = LoginPage()
# login_page.open()
# login_page.click()
# login_page.login('admin', 'admin')
login_page.verify_text()
