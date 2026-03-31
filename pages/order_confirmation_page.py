from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
import time


class OrderConfirmationPage(BasePage):
    CONFIRMATION_MODAL = (By.CSS_SELECTOR, ".Order_Modal__YZd3G")
    SUCCESS_TEXT = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Проверить успешное создание заказа")
    def is_order_successfully_created(self):
        time.sleep(2)
        return self.is_element_displayed(self.CONFIRMATION_MODAL) or self.is_element_displayed(self.SUCCESS_TEXT)