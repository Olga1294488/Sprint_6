from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderConfirmationPage(BasePage, OrderPageLocators):
    
    def is_order_successfully_created(self):
        return self.wait_for_visible(self.CONFIRMATION_MODAL).is_displayed()