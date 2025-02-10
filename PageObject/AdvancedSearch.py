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
        self.block_search_for_an_actor_director_screenwriter_button_search = (By.XPATH, "//*[contains(@class, 'el_8 submit nice_button')]")
        self.block_search_for_an_actor_director_screenwriter_first_name_or_last_name = (By.XPATH, "//*[contains(@id, 'find_people')]")


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


    @allure.step("Нажать кнопку 'Поиск' в блоке 'Искать актера/режиссера/сценариста/...'")
    def click_block_search_for_an_actor_director_screenwriter_button(self):
        """
        Эта функция нажимает кнопку "Поиск" в блоке "Искать актера/режиссера/сценариста/..." и возвращает из результата поиска часть текста в формате "поиск: <зим> • результаты: <1429>"
        """
        self.driver.find_element(*self.block_search_for_an_actor_director_screenwriter_button_search).click()
        self.driver.implicitly_wait(10)
        text = self.driver.find_element(*self.search_results).text
        return text


    @allure.step("Заполнить поле 'имя/фамилия' в блоке 'Искать актера/режиссера/сценариста/...'")
    def fill_block_search_for_an_actor_director_screenwriter_first_name_or_last_name(self, first_name_or_last_name: str)  -> None:
        """
        Эта функция заполняет поле 'имя/фамилия' в блоке "Искать актера/режиссера/сценариста/..."
        """
        self.driver.find_element(*self.block_search_for_an_actor_director_screenwriter_first_name_or_last_name).send_keys(first_name_or_last_name)