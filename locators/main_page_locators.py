from selenium.webdriver.common.by import By


class MainPageLocators:

    BUTTON_ORDER_UP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']") # Кнопка "Заказать" в шапке
    BUTTON_ORDER_LOW = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']") # Кнопки "Заказать" внизу страницы
    BUTTON_COOKIES = (By.ID, "rcc-confirm-button") # Кнопки куки "Да все привыкли"
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']") # Логотип "Самокат"
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']") # Логотип "Яндекс"
    
    # Вопросы
    QUESTION = "accordion__heading-{}"

    # Ответы
    ANSWER = "//div[@id='accordion__panel-{}']/p"