from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.actions = ActionChains(driver)
    
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element
    
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return element
    
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element
    
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    def is_element_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except TimeoutException:
            return False
    
    def switch_to_new_window(self):
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        return original_window
    
    @allure.step("Открыть страницу {url}")
    def open_page(self, url):
        self.driver.get(url)
    
    def get_current_url(self):
        return self.driver.current_url