from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

SEARCH_CIRCLE = By.CSS_SELECTOR,"#utilityNav-circle"
RESULTS = By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']"

class CirclePage(BasePage):

    def click_circle_button(self):
        self.click(self,*SEARCH_CIRCLE)

    def find_element(self,*RESULTS):
        print('Searching by {*RESULTS}')



