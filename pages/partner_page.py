from pages.base_page import Page


class PartnerPage(Page):

    # Android Google PLay
    def verify_google_play_opened(self):
        self.verify_partial_url('https://play.google.com/')

