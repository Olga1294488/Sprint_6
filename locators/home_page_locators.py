from selenium.webdriver.common.by import By


class HomePageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[text()='Заказать']")
    ACCORDION_BUTTON = (By.CLASS_NAME, "accordion__button")
    ACCORDION_PANEL = (By.CLASS_NAME, "accordion__panel")
    VISIBLE_ACCORDION_PANEL = (By.CSS_SELECTOR, ".accordion__panel:not([hidden])")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")