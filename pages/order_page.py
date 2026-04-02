from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By


class OrderPage(BasePage, OrderPageLocators):
    
    def fill_first_form(self, name, surname, address, metro, phone):
        self.input_text(self.NAME_INPUT, name)
        self.input_text(self.SURNAME_INPUT, surname)
        self.input_text(self.ADDRESS_INPUT, address)
        
        self.click(self.METRO_INPUT)
        metro_option = (By.XPATH, f"//div[contains(text(), '{metro}')]")
        option = self.wait.until(lambda d: d.find_element(*metro_option))
        self.click_js(option)
        
        self.input_text(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)
        self.wait.until(lambda d: d.find_element(*self.DATE_INPUT))
    
    def fill_second_form(self, date, period, color, comment):
        date_input = self.find_element(self.DATE_INPUT)
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys("\n")
        
        self.click(self.RENTAL_PERIOD)
        period_option = (By.XPATH, f"//div[contains(text(), '{period}')]")
        option = self.wait.until(lambda d: d.find_element(*period_option))
        self.click_js(option)
        
        if color == "black":
            self.click(self.COLOR_BLACK)
        else:
            self.click(self.COLOR_GREY)
        
        if comment:
            self.input_text(self.COMMENT_INPUT, comment)
        
        self.click(self.ORDER_BUTTON)
        self.wait.until(lambda d: d.find_element(*self.CONFIRM_BUTTON))
    
    def confirm(self):
        self.click(self.CONFIRM_BUTTON)
        self.wait.until(lambda d: d.find_element(*self.SUCCESS_MODAL))
    
    def is_success(self):
        return self.find_element(self.SUCCESS_MODAL).is_displayed()