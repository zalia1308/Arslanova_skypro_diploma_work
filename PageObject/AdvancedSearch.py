from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import allure


class AdvancedSearch:
    """
    Этот класс представляет страницу "Расширенный поиск" сайта "Кинопоиск"
    """
    def __init__(self, driver):
        self.driver = driver
        self.search_results = (By.XPATH, "//*[contains(@class, 'search_results_topText')]")
        self.block_search_for_a_movie_button_search = (By.XPATH, "//*[contains(@class, 'el_18 submit nice_button')]")
        self.block_search_for_a_movie_field_name_of_film = (By.XPATH, "//*[contains(@class, 'text el_1')]")
        self.block_search_for_a_movie_field_genre = (By.XPATH, "//*[contains(@class, 'text el_6 __genreSB__')]")
        self.block_search_for_a_movie_field_country = (By.XPATH, "//*[contains(@class, 'text el_5 __countrySB__')]")
        self.block_search_for_by_creators_button_search = (By.XPATH, "//*[contains(@id, 'btn_search_6')]")
        self.block_search_for_by_creators_field_type = (By.XPATH, "//*[contains(@id, 'cr_search_field_1_select')]")
        self.block_search_for_by_creators_field_input_box = (By.XPATH, "//*[contains(@id, 'cr_search_field_1')]")
        self.block_search_for_by_creators_field_input_box_dropdown_locator = (By.XPATH, "//*[contains(@class, 'ui - menu - item')]")


    @allure.step("Нажать кнопку 'Поиск' в блоке 'Искать фильм:'")
    def click_block_search_for_a_movie_button(self):
        """
        Эта функция нажимает кнопку "Поиск" в блоке "Искать фильм:" и возвращает из результата поиска часть текста в формате "поиск: <зим> • результаты: <1429>"
        """
        self.driver.find_element(*self.block_search_for_a_movie_button_search).click()
        self.driver.implicitly_wait(10)
        text = self.driver.find_element(*self.search_results).text
        return text


    @allure.step("Заполнить поле 'полное или частичное название фильма' в блоке 'Искать фильм:'")
    def fill_block_search_for_a_movie_field_name_of_film(self, name_of_film: str)  -> None:
        """
        Эта функция заполняет поле "полное или частичное название фильма" в блоке "Искать фильм:"
        """
        self.driver.find_element(*self.block_search_for_a_movie_field_name_of_film).send_keys(name_of_film)


    @allure.step("Выбрать значение в поле '+ жанр:' в блоке 'Искать фильм:'")
    def fill_block_search_for_a_movie_field_genre(self, genre: str)  -> None:
        """
        Эта функция заполняет поле "+ жанр:" в блоке "Искать фильм:"
        """
        dropdown_element = self.driver.find_element(*self.block_search_for_a_movie_field_genre)
        select = Select(dropdown_element)
        select.select_by_visible_text(genre)


    @allure.step("Нажать на поле '+ страна:' в блоке 'Искать фильм:' и выбрать значение в выпадающем списке")
    def fill_block_search_for_a_movie_field_country(self, country: str)  -> None:
        """
        Эта функция заполняет поле "+ страна:" в блоке "Искать фильм:"
        """
        dropdown_element = self.driver.find_element(*self.block_search_for_a_movie_field_country)
        select = Select(dropdown_element)
        select.select_by_visible_text(country)


    @allure.step("Нажать кнопку 'Поиск' в блоке 'Искать фильм по создателям:'")
    def click_block_search_by_creators_button(self):
        """
        Эта функция нажимает кнопку "Поиск" в блоке "Искать фильм по создателям:" и возвращает из результата поиска часть текста в формате "поиск: <зим> • результаты: <1429>"
        """
        self.driver.find_element(*self.block_search_for_by_creators_button_search).click()
        self.driver.implicitly_wait(10)
        text = self.driver.find_element(*self.search_results).text
        return text


    @allure.step("Заполнить поля в блоке 'Искать фильм по создателям:'")
    def fill_block_search_for_by_creators_boxs(self, type_person: str, text_to_search: str, person: str)  -> None:
        """
        Эта функция заполняет поля в блоке "Искать фильм по создателям:"
        """
        with allure.step("Нажать на первое поле в первой строке и выбрать значение {type_person}"):
            dropdown_element = self.driver.find_element(*self.block_search_for_by_creators_field_type)
            select = Select(dropdown_element)
            select.select_by_visible_text(type_person)
        with allure.step("Нажать на второе поле в первой строке и ввести значение {text_to_search} для поиска в выпадающем списке"):
            self.driver.find_element(*self.block_search_for_by_creators_field_input_box).send_keys(text_to_search)
            dropdown_item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(f"{self.block_search_for_by_creators_field_input_box_dropdown_locator}[text()='{person}']"))
        with allure.step("Нажать на значение {person} в результате поиска в выпадающем списке поля"):
            dropdown_item.click()