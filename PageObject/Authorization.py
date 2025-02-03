from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import url
import allure


class Authorization:
    """
    Этот класс представляет страницу авторизации сайта "Кинопоиск"
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(url)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.button_enter_personal_account = (By.XPATH, "//button[contains(@class, 'styles_loginButton__LWZQp')]")
        self.yandex_login = (By.CSS_SELECTOR, "#passp-field-login")
        self.yandex_button_enter_after_login = (By.CSS_SELECTOR, "#passp\:sign-in")
        self.yandex_password = (By.CSS_SELECTOR, "#passp-field-passwd")
        self.yandex_button_continue_after_password = (By.CSS_SELECTOR, "#passp\:sign-in")
        self.button_element_from_the_main_page = (By.XPATH, "//*[contains(@class, 'styles_root__7mPJN styles_lightThemeItem__BSbZW')]")


    @allure.step("Авторизоваться на сайте Кинопоиска")
    def authorization(self, login: str, password: str)  -> None:
        """
        Эта функция выполняет авторизацию на сайте "Кинопоиск"
        """
        with allure.step("Нажать кнопку 'Войти'"):
            self.driver.find_element(*self.button_enter_personal_account).click()
            self.driver.implicitly_wait(20)
        with allure.step("Заполнить поле 'Логин или email'"):
            self.driver.find_element(*self.yandex_login).send_keys(login)
        with allure.step("Нажать кнопку 'Войти'"):
            self.driver.find_element(*self.yandex_button_enter_after_login).click()
            WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(self.yandex_password))
        with allure.step("Заполнить поле 'Введите пароль'"):
            self.driver.find_element(*self.yandex_password).send_keys(password)
        with allure.step("Нажать кнопку 'Продолжить'"):
            self.driver.find_element(*self.yandex_button_continue_after_password).click()
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.button_element_from_the_main_page))