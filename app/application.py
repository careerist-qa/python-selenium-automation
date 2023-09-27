from pages.main_page import MainPage
from pages.header import Header

class Application:
    def __init__(self,driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)

app = Application()
app.main_page.MainPage()
app.header.search_product()