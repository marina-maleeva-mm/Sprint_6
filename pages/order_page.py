import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):
    
    @allure.step("Заполнить поле 'Имя'")
    def enter_first_name(self, name):
        self.send_keys_to_field(OrderPageLocators.FIELD_FIRST_NAME, name)

    @allure.step("Заполнить поле 'Фамилия'")
    def enter_last_name(self, last_name):
        self.send_keys_to_field(OrderPageLocators.FIELD_LAST_NAME, last_name)

    @allure.step("Заполнить поле 'Адрес'")
    def set_address(self, address):
        self.send_keys_to_field(OrderPageLocators.FIELD_ADDRESS, address)

    @allure.step("Выбрать станцию метро: {station_name}")
    def select_metro_station(self, station_name):
        self.click_on_locator(OrderPageLocators.FIELD_METRO)
        metro_locator = OrderPageLocators.METRO_STATION.format(station=station_name)
        self.find_element_with_dynamic_xpath(metro_locator).click()

    @allure.step("Заполнить поле 'Телефон'")
    def enter_phone(self, phone):
        self.send_keys_to_field(OrderPageLocators.FIELD_PHONE, phone)

    @allure.step("Клик по кнопке 'Далее'")
    def click_next_button(self):
        self.click_on_locator(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Выбор даты")
    def set_date(self, date):
        field = self.find_and_wait_locator(OrderPageLocators.FIELD_DATA)
        field.click()
        field.send_keys(date)
        field.send_keys(Keys.ENTER)

    @allure.step("Выбор срока аренды")
    def set_rent_duration(self):
        self.click_on_locator(OrderPageLocators.FIELD_RENT)
        self.click_on_locator(OrderPageLocators.SELECT_RENT)

    @allure.step("Выбор цвета самоката 'Черный'")
    def select_color_black(self):
        self.click_on_locator(OrderPageLocators.BLACK_CHECKBOX)

    @allure.step("Выбор цвета самоката 'Серый'")
    def select_color_grey(self):
        self.click_on_locator(OrderPageLocators.GREY_CHECKBOX)

    @allure.step("Ввод комментария: {comment}")
    def add_comment(self, comment):
        self.send_keys_to_field(OrderPageLocators.FIELD_MESSAGE, comment)

    @allure.step("Клик по кнопке 'Заказать'")
    def click_button_order(self):
        self.click_on_locator(OrderPageLocators.BUTTON_ORDER)

    @allure.step("Подтверждение заказа")
    def click_button_yes(self):
        self.click_on_locator(OrderPageLocators.BUTTON_YES)

    @allure.step("Проверка, что заказ оформлен")
    def order_completed(self):
        return self.find_and_wait_locator(OrderPageLocators.ORDER_OK).is_displayed()

    @allure.step("Полный процесс оформления заказа самоката 'Верхняя кнопка'")
    def complete_scooter_order(self, user_data):
        self.enter_first_name(user_data.first_name)  # Заполнить Имя
        self.enter_last_name(user_data.last_name)  # Заполнить фамилию
        self.set_address(user_data.address)  # Заполнить адрес
        self.select_metro_station(user_data.metro_station)  # Заполнить станцию метро
        self.enter_phone(user_data.tel)  # Заполнить поле Телефон
        self.click_next_button()  # Клик на кнопку Далее
        self.set_date(user_data.delivery_data)  # Выбор даты
        self.set_rent_duration()  # Выбор срока аренды
        self.select_color_black() # Выбор цвета самоката
        self.add_comment(user_data.message)  # Ввод комментария
        self.click_button_order()  # Клик на кнопку 'Заказать'
        self.click_button_yes()  # Подтверждение заказа