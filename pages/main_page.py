import allure
from data import Urls
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.MAIN_PAGE

    @allure.step("Принять куки")
    def accept_cookies(self):
        if self.is_element_visible(MainPageLocators.BUTTON_COOKIES):
            self.click_on_locator(MainPageLocators.BUTTON_COOKIES)

    @allure.step("Клик по кнопке 'Заказать' вверху страницы")
    def click_button_order_up(self):
        self.click_on_locator(MainPageLocators.BUTTON_ORDER_UP)

    @allure.step("Клик по кнопке 'Заказать' внизу страницы")
    def click_button_order_low(self):
        self.scroll_to_locator(MainPageLocators.BUTTON_ORDER_LOW)
        self.click_on_locator(MainPageLocators.BUTTON_ORDER_LOW)


    @allure.step("Кликнуть по вопросу")
    def expand_faq_question(self, index):
        locator = (By.ID, MainPageLocators.QUESTION.format(index))
        self.click_on_locator(locator)

    @allure.step("Получить текст ответа")
    def get_faq_answer(self, index):
        locator = (By.XPATH, MainPageLocators.ANSWER.format(index))
        return self.get_text(locator)
    
    @allure.step("Клик по лого 'Яндекс'")
    def click_yandex_logo(self):
        self.click_on_locator(MainPageLocators.LOGO_YANDEX)


    @allure.step("Проверить клик по лого 'Самокат'")
    def click_scooter_logo(self):
        self.click_on_locator(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Проверить, что открыта страница Дзена")
    def wait_for_dzen_opened(self):
        self.wait_for_url_contains("dzen.ru")