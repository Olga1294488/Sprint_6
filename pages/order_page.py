from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure
import time


class OrderPage(BasePage):
    # Локаторы первой формы
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Локаторы второй формы
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_INPUT = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder')]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_js(self, element):
        """Клик через JavaScript"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", element)
    
    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self, name, surname, address, metro_station, phone):
        time.sleep(1)
        
        # Имя
        name_input = self.wait.until(EC.presence_of_element_located(self.NAME_INPUT))
        name_input.clear()
        name_input.send_keys(name)
        
        # Фамилия
        surname_input = self.wait.until(EC.presence_of_element_located(self.SURNAME_INPUT))
        surname_input.clear()
        surname_input.send_keys(surname)
        
        # Адрес
        address_input = self.wait.until(EC.presence_of_element_located(self.ADDRESS_INPUT))
        address_input.clear()
        address_input.send_keys(address)
        
        # Станция метро
        metro_input = self.wait.until(EC.element_to_be_clickable(self.METRO_STATION_INPUT))
        metro_input.click()
        time.sleep(1)
        
        metro_option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[contains(text(), '{metro_station}')]")))
        metro_option.click()
        time.sleep(1)
        
        # Телефон
        phone_input = self.wait.until(EC.presence_of_element_located(self.PHONE_INPUT))
        phone_input.clear()
        phone_input.send_keys(phone)
        time.sleep(1)
        
        # Кнопка "Далее"
        next_btn = self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
        self.click_js(next_btn)
        time.sleep(2)
    
    @allure.step("Заполнить вторую форму заказа")
    def fill_second_form(self, delivery_date, rental_period, color, comment):
        time.sleep(1)
        
        # Дата доставки
        date_input = self.wait.until(EC.presence_of_element_located(self.DELIVERY_DATE_INPUT))
        date_input.clear()
        date_input.send_keys(delivery_date)
        date_input.send_keys("\n")
        time.sleep(2)
        
        # Срок аренды
        period_input = self.wait.until(EC.element_to_be_clickable(self.RENTAL_PERIOD_INPUT))
        period_input.click()
        time.sleep(1)
        
        period_option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[contains(text(), '{rental_period}')]")))
        period_option.click()
        time.sleep(1)
        
        # Цвет самоката
        if color == "black":
            color_checkbox = self.wait.until(EC.element_to_be_clickable(self.COLOR_BLACK))
            self.click_js(color_checkbox)
        elif color == "grey":
            color_checkbox = self.wait.until(EC.element_to_be_clickable(self.COLOR_GREY))
            self.click_js(color_checkbox)
        time.sleep(1)
        
        # Комментарий
        if comment:
            comment_input = self.wait.until(EC.presence_of_element_located(self.COMMENT_INPUT))
            comment_input.clear()
            comment_input.send_keys(comment)
        
        time.sleep(1)
        
        # Кнопка "Заказать"
        order_btn = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON))
        self.click_js(order_btn)
        time.sleep(2)
    
    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        confirm_btn = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON))
        self.click_js(confirm_btn)
        time.sleep(3)