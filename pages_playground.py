class BasePage:


    def find_el(self):
        print("Finding element")

    def click(self):
        print("Clicking element")


    def verify_text(self, expected_text):
        print(f'Checking for: {expected_text}')

class LoginPage(BasePage):
    def __init__(self):
        self.default_pw = 'password'
    def login(self, email,pw):
        print("login...")

    def verify_TC(self):
        self.verify_text('TC text')

class RegularPage(BasePage):
    print("Registering...")

login_page = LoginPage()
reg_page = RegularPage()
#login_page.login()
login_page.click()

print(login_page.default_pw)