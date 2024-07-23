from pages.hw6_base_page import Hw6Page


class Hw6MainPage(Hw6Page):
    TARGET_URL = 'https://www.target.com/'

    def open(self):
        self.open_url(self.TARGET_URL)
