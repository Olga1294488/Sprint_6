import pytest
import allure
from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.order_confirmation_page import OrderConfirmationPage
import time


@allure.feature("Оформление заказа")
class TestOrder:
    
    @pytest.mark.parametrize("button_type,name,surname,address,metro_station,phone,delivery_date,rental_period,color,comment", [
        ("top", "Анна", "Петрова", "ул. Ленина, 10", "Сокольники", "89991234567", "01.12.2024", "сутки", "black", "Позвоните за 15 минут"),
        ("bottom", "Иван", "Сидоров", "пр. Мира, 25", "Красносельская", "89876543210", "02.12.2024", "двое суток", "grey", "Домофон 123")
    ])
    @allure.title("Позитивный сценарий заказа самоката (кнопка: {button_type})")
    def test_create_order(self, driver, button_type, name, surname, address, metro_station, 
                          phone, delivery_date, rental_period, color, comment):
        home_page = HomePage(driver)
        time.sleep(2)
        
        # Нажимаем кнопку заказа
        if button_type == "top":
            # Верхняя кнопка
            top_button = driver.find_element(*home_page.ORDER_BUTTON_TOP)
            driver.execute_script("arguments[0].scrollIntoView(true);", top_button)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", top_button)
        else:
            # Нижняя кнопка - скроллим вниз
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            bottom_button = driver.find_element(*home_page.ORDER_BUTTON_BOTTOM)
            driver.execute_script("arguments[0].scrollIntoView(true);", bottom_button)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", bottom_button)
        
        time.sleep(2)
        
        # Заполняем форму заказа
        order_page = OrderPage(driver)
        order_page.fill_first_form(name, surname, address, metro_station, phone)
        order_page.fill_second_form(delivery_date, rental_period, color, comment)
        order_page.confirm_order()
        
        time.sleep(3)
        
        # Проверяем успешное создание заказа
        confirmation_page = OrderConfirmationPage(driver)
        assert confirmation_page.is_order_successfully_created(), "Заказ не был создан успешно"