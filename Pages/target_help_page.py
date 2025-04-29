from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

class TargetHelpPage(BasePage):
    DD = (By.CSS_SELECTOR, "[name='j_id0:contentTemplate:j_id79:j_id80:viewHelpTopics:ViewHelpTopics']")

    def open_target_help_page(self):
        self.open_url("https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges")
        sleep(5)

    def verify_help_page_opened(self):
        self.verify_url("https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges")

    def select_topic_target_help_page(self):
        dropdown = self.find_element(*self.DD)
        select = Select(dropdown)
        select.select_by_value('Orders & Purchases')
        sleep(5)

    def verify_orders_and_purchases_opened(self):
        self.verify_url("https://help.target.com/help/SubCategoryArticle?childcat=Print+a+receipt&parentcat=Orders+%26+Purchases&searchQuery=")






