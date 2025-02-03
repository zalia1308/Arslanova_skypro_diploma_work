from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    """
    Этот класс представляет главную страницу сайта "Кинопоиск"
    """
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.XPATH, "//*[contains(@class, 'styles_inputActive__ICcod styles_input__4vNAb kinopoisk-header-search-form-input__input')]")
        self.search_header_positive = (By.XPATH, "//*[contains(@class, 'styles_title__irLOv kinopoisk-header-suggest-group__title')]")
        self.search_header_negative = (By.XPATH, "//*[contains(@class, 'styles_emptySuggest__XEkB0')]")
        self.button_open_advanced_search = (By.XPATH, "//*[contains(@class, 'styles_advancedSearch__uwvnd')]")
        self.advanced_search = (By.XPATH, "//*[contains(@class, 'text-orange')]")


    @allure.step("Выполнить поиск с валидными данными {input_box} через поисковую строку")
    def search_bar_positive(self, input_box: str)  -> str:
        """
        Эта функция выполняет поиск с валидными данными в поисковой строке
        """
        self.driver.find_element(*self.search_bar).send_keys(input_box)
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(self.search_header_positive,"Возможно, вы искали"))
        text = self.driver.find_element(*self.search_header_positive).text
        return text


    @allure.step("Выполнить поиск с невалидными данными {input_box} через поисковую строку")
    def search_bar_negative(self, input_box: str)  -> str:
        """
        Эта функция выполняет поиск с невалидными данными в поисковой строке
        """
        self.driver.find_element(*self.search_bar).send_keys(input_box)
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(self.search_header_negative,"По вашему запросу ничего не найдено"))
        text = self.driver.find_element(*self.search_header_negative).text
        return text


    @allure.step("Нажать кнопку ввиде 2-х линий с точками в поисковой строке")
    def open_advanced_search(self)  -> None:
        """
        Эта функция выполняет переход к странице "Расширенный поиск" при нажатии кнопки в поисковой строке из главной страницы
        """
        self.driver.find_element(*self.button_open_advanced_search).click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.advanced_search, 'Расширенный поиск'))