from pages.base_page import BasePage

class MainPage(Page):
    def open_main(self):
        self.driver.get('https://www.target.com/')
        context.app.main_page.open_main_page()


