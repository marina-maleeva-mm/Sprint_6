import pytest
import allure
from data import User_1, User_2
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestScooterOrder:
    
    @allure.title("Проверка оформления заказа самоката")
    @pytest.mark.parametrize(
        "order_button, user_data",
        [
            ("up", User_1),
            ("low", User_2)
        ]
    )
    
    def test_scooter_order(self, driver, order_button, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.accept_cookies()

        if order_button == "up":
            main_page.click_button_order_up()
        elif order_button == "low":
            main_page.click_button_order_low()

        order_page.complete_scooter_order(user_data)

        assert order_page.order_completed()