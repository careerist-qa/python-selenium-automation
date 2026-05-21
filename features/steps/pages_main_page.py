 from time import sleep
 from pages.base_page import Page
 class MainPage(Page):

 def open_main(self):
  self.open_url()
  sleep(2)


