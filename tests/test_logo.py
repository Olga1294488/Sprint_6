from pages.home_page import HomePage


class TestLogo:
    
    def test_scooter_logo(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_top()
        home_page.click_scooter_logo()
        assert "qa-scooter" in home_page.get_current_url()
    
    def test_yandex_logo(self, driver):
        home_page = HomePage(driver)
        original_window = driver.current_window_handle
        home_page.click_yandex_logo()
        home_page.wait.until(lambda d: len(d.window_handles) > 1)
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
        current_url = driver.current_url
        driver.close()
        driver.switch_to.window(original_window)
        assert "dzen.ru" in current_url