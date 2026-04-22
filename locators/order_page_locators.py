from selenium.webdriver.common.by import By


class OrderPageLocators:
    # ФОРМА "Для кого самокат"
    FIELD_FIRST_NAME = (By.XPATH, '//input[@placeholder="* Имя"]') # Поле "Имя"
    FIELD_LAST_NAME = (By.XPATH, '//input[@placeholder="* Фамилия"]') # Поле "Фамилия"
    FIELD_ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]') # Поле "Адрес: куда привезти"
    FIELD_METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]') # Поле "Станция метро"
    METRO_STATION = '//div[@class="select-search__select"]//div[text()="{station}"]' # Станция метро
    FIELD_PHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]') # Поле "Телефон: на него позвонит курьер"

    BUTTON_NEXT = (By.XPATH, './/button[text()="Далее"]') # Кнопка "Далее"

    # Форма "Про аренду"
    FIELD_DATA = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]') # Поле "Когда привезти самокат"
    SELECT_DATE = (By.XPATH, '//div[@aria-label="Choose пятница, 31-е октября 2025 г."]') # Выбор даты
    FIELD_RENT = (By.XPATH, './/div[text()="* Срок аренды"]') # Поле "Срок аренды"
    SELECT_RENT = (By.XPATH, './/div[text()="сутки"]') # Выбор срока аренды
    BLACK_CHECKBOX = (By.ID, 'black') # Цвет - "чёрный жемчуг"
    GREY_CHECKBOX = (By.ID, 'grey') # Цвет - "серая безысходность"
    FIELD_MESSAGE = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]') # Поле "Комментарий для курьера"

    BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[contains(@class, 'Button_Middle') and text()='Заказать']") # Кнопка "Заказать"

    # Окно "Хотите оформить заказ?"
    BUTTON_NO = (By.XPATH, './/button[text()="Нет"]') # Кнопка "Нет"
    BUTTON_YES = (By.XPATH, './/button[text()="Да"]') # Кнопка "Да"

   # Окно "Заказ оформлен"
    ORDER_OK = (By.XPATH, './/div[text()="Заказ оформлен"]') # Подтверждение заказа
    BUTTON_STATUS = (By.XPATH, './/div[text()="Посмотреть статус"]') # Кнопка "Посмотреть статус"

    # Логотипы
    LOGO_SCOOTER = (By.XPATH, ".//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, ".//img[@alt='Yandex']")