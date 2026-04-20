import allure
from data import Urls
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.MAIN_PAGE

    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click_on_locator(MainPageLocators.BUTTON_COOKIES)
        except Exception:
            pass

    @allure.step("Клик по кнопке 'Заказать' вверху страницы")
    def click_button_order_up(self):
        self.click_on_locator(MainPageLocators.BUTTON_ORDER_UP)

    @allure.step("Клик по кнопке 'Заказать' внизу страницы")
    def click_button_order_low(self):
        self.scroll_to_locator(MainPageLocators.BUTTON_ORDER_LOW)
        self.click_on_locator(MainPageLocators.BUTTON_ORDER_LOW)

    @allure.step("Клик на вопрос № {question_number}")
    def expand_faq_question(self, question_number):
        
        questions = [
            MainPageLocators.QUESTION_1,
            MainPageLocators.QUESTION_2, 
            MainPageLocators.QUESTION_3,
            MainPageLocators.QUESTION_4,
            MainPageLocators.QUESTION_5,
            MainPageLocators.QUESTION_6,
            MainPageLocators.QUESTION_7,
            MainPageLocators.QUESTION_8
        ]
        self.scroll_to_locator(questions[question_number])
        self.click_on_locator(questions[question_number])

    @allure.step("Получить ответ №{answer_number}")
    def get_faq_answer(self, answer_number):
        answer = [
            MainPageLocators.ANSWER_1,
            MainPageLocators.ANSWER_2,
            MainPageLocators.ANSWER_3,
            MainPageLocators.ANSWER_4,
            MainPageLocators.ANSWER_5,
            MainPageLocators.ANSWER_6,
            MainPageLocators.ANSWER_7,
            MainPageLocators.ANSWER_8
        ]
        return self.get_element_text(answer[answer_number])
    
    @allure.step("Клик по лого 'Яндекс'")
    def click_yandex_logo(self):
        self.click_on_locator(OrderPageLocators.LOGO_YANDEX)


    @allure.step("Проверить клик по лого 'Самокат'")
    def click_scooter_logo(self):
        self.click_on_locator(OrderPageLocators.LOGO_SCOOTER)

    @allure.step("Проверить, что открыта страница Дзена")
    def is_dzen_opened(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.url_contains("dzen.ru"))
            return True
        except Exception:
            return False