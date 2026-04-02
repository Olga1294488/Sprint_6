from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage, HomePageLocators):
    
    def click_order_top(self):
        button = self.find_element(self.ORDER_BUTTON_TOP)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)
    
    def click_order_bottom(self):
        button = self.find_element(self.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)
    
    def click_question(self, index):
        questions = self.find_elements(self.ACCORDION_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", questions[index])
        self.driver.execute_script("arguments[0].click();", questions[index])
    
    def get_answer_text(self):
        panel = self.wait.until(EC.visibility_of_element_located(self.VISIBLE_ACCORDION_PANEL))
        return panel.text
    
    def click_scooter_logo(self):
        logo = self.find_element(self.SCOOTER_LOGO)
        logo.click()
    
    def click_yandex_logo(self):
        logo = self.find_element(self.YANDEX_LOGO)
        logo.click()
    
    def get_current_url(self):
        return self.driver.current_url