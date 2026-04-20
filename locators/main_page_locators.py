from selenium.webdriver.common.by import By


class MainPageLocators:

    BUTTON_ORDER_UP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']") # Кнопка "Заказать" в шапке
    BUTTON_ORDER_LOW = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']") # Кнопки "Заказать" внизу страницы
    BUTTON_COOKIES = (By.ID, "rcc-confirm-button") # Кнопки куки "Да все привыкли"
    
    # Вопросы
    QUESTION_1 = (By.ID, "accordion__heading-0")
    QUESTION_2 = (By.ID, "accordion__heading-1")
    QUESTION_3 = (By.ID, "accordion__heading-2")
    QUESTION_4 = (By.ID, "accordion__heading-3")
    QUESTION_5 = (By.ID, "accordion__heading-4")
    QUESTION_6 = (By.ID, "accordion__heading-5")
    QUESTION_7 = (By.ID, "accordion__heading-6")
    QUESTION_8 = (By.ID, "accordion__heading-7")

    # Ответы
    ANSWER_1 = (By.XPATH, ".//div[@id='accordion__panel-0']/p")
    ANSWER_2 = (By.XPATH, ".//div[@id='accordion__panel-1']/p")
    ANSWER_3 = (By.XPATH, ".//div[@id='accordion__panel-2']/p")
    ANSWER_4 = (By.XPATH, ".//div[@id='accordion__panel-3']/p")
    ANSWER_5 = (By.XPATH, ".//div[@id='accordion__panel-4']/p")
    ANSWER_6 = (By.XPATH, ".//div[@id='accordion__panel-5']/p")
    ANSWER_7 = (By.XPATH, ".//div[@id='accordion__panel-6']/p")
    ANSWER_8 = (By.XPATH, ".//div[@id='accordion__panel-7']/p")