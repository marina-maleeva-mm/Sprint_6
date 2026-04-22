import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver   
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть главную страницу")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Поиск и ожидание элемента")
    def find_and_wait_locator(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    @allure.step("Поиск и ожидание видимого элемента")
    def find_visible_element(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))
    
    @allure.step("Кликнуть по элементу")
    def click_on_locator(self, locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввод данных в поле")
    def send_keys_to_field(self, locator, text):
        self.find_and_wait_locator(locator).send_keys(text)

    @allure.step("Получить текст элемента")
    def get_element_text(self, locator):
        return self.find_visible_element(locator).text
    
    @allure.step("Прокрутка до элемента")
    def scroll_to_locator(self, locator):
        element = self.find_and_wait_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Перейти на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Проверить, что элемент виден")
    def is_element_visible(self, locator):
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0 and elements[0].is_displayed()

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.find_visible_element(locator).text

    @allure.step("Найти элемент по динамическому XPath")
    def find_element_with_dynamic_xpath(self, xpath):
        return self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

    @allure.step("Открыть страницу")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Дождаться, что URL содержит текст")
    def wait_for_url_contains(self, text):
        self.wait.until(expected_conditions.url_contains(text))
        