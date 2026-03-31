from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure
import time


class HomePage(BasePage):
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Button') and contains(@class, 'Middle') and text()='Заказать']")
    ACCORDION_BUTTON = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemButton']")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']/..")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']/..")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Нажать кнопку заказа вверху страницы")
    def click_order_button_top(self):
        button = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_TOP))
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
    
    @allure.step("Нажать кнопку заказа внизу страницы")
    def click_order_button_bottom(self):
        button = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_BOTTOM))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
    
    @allure.step("Нажать на вопрос {index}")
    def click_question_button(self, index):
        questions = self.driver.find_elements(*self.ACCORDION_BUTTON)
        if len(questions) > index:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", questions[index])
            time.sleep(1)
            questions[index].click()
            time.sleep(1)
    
    @allure.step("Получить текст ответа на вопрос {index}")
    def get_answer_text(self, index):
        answer_locator = (By.XPATH, f"//div[@data-accordion-component='AccordionItemPanel' and not(@hidden)]")
        self.wait.until(lambda d: d.find_element(*answer_locator).is_displayed())
        return self.driver.find_element(*answer_locator).text
    
    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(self.SCOOTER_LOGO))
        logo.click()
        time.sleep(1)
    
    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(self.YANDEX_LOGO))
        logo.click()
        time.sleep(2)
    
    def get_current_url(self):
        return self.driver.current_url