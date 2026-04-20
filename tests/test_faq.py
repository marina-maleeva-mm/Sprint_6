import allure
import pytest
from pages.main_page import MainPage
from data import Urls, FAQ_ANSWER

class TestFAQ:
    @allure.title("Проверка блока Вопросы о важном")
    @allure.description("При нажатии на вопрос - открывается ответ")
    @pytest.mark.parametrize("index, expected_text", list(enumerate(FAQ_ANSWER)))
    def test_faq_answers(self, driver, index, expected_text):
        main_page = MainPage(driver)
        main_page.go_to_url(Urls.MAIN_PAGE)
        main_page.accept_cookies()
        main_page.expand_faq_question(index)
        answer = main_page.get_faq_answer(index)

        assert expected_text.strip() == answer.strip()