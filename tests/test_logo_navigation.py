import allure
from pages.home_page import HomePage
import time


@allure.feature("Навигация по логотипам")
class TestLogoNavigation:
    """Тесты для проверки переходов по логотипам"""
    
    @allure.title("Проверка перехода на главную страницу по логотипу «Самоката»")
    @allure.description("При нажатии на логотип «Самоката» происходит переход на главную страницу")
    def test_scooter_logo_navigation(self, driver):
        """Тест перехода на главную страницу по логотипу Самоката"""
        home_page = HomePage(driver)
        time.sleep(1)
        
        # Переходим на страницу заказа
        home_page.click_order_button_top()
        time.sleep(1)
        
        # Кликаем на логотип Самоката
        home_page.click_scooter_logo()
        time.sleep(1)
        
        # Проверяем, что вернулись на главную страницу
        current_url = home_page.get_current_url()
        assert "qa-scooter.praktikum-services.ru" in current_url, \
            f"Не произошло возврата на главную страницу. Текущий URL: {current_url}"
    
    @allure.title("Проверка перехода на страницу Дзена по логотипу Яндекса")
    @allure.description("При нажатии на логотип Яндекса открывается страница Дзена в новом окне")
    def test_yandex_logo_navigation(self, driver):
        """Тест перехода на Дзен по логотипу Яндекса"""
        home_page = HomePage(driver)
        time.sleep(1)
        
        # Кликаем на логотип Яндекса
        home_page.click_yandex_logo()
        time.sleep(3)
        
        # Переключаемся на новую вкладку
        original_window = driver.current_window_handle
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        
        time.sleep(2)
        
        # Проверяем, что открылась страница Дзена
        current_url = driver.current_url
        assert "dzen.ru" in current_url or "yandex.ru" in current_url, \
            f"Не произошло перехода на Дзен. Текущий URL: {current_url}"
        
        # Закрываем вкладку и возвращаемся
        driver.close()
        driver.switch_to.window(original_window)