import pytest
import allure
from data import User_1, User_2
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestScooterOrder:
    
    @allure.title("Проверка оформления заказа самоката")
    @pytest.mark.parametrize(
        "click_order_button, user_data",
        [
            pytest.param(MainPage.click_button_order_up, User_1, id="order_from_upper_button"),
            pytest.param(MainPage.click_button_order_low, User_2, id="order_from_lower_button"),
        ]
    )
    
    def test_scooter_order(self, driver, click_order_button, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.accept_cookies()
        click_order_button(main_page)

        order_page.complete_scooter_order(user_data)

        assert order_page.order_completed()