from selenium import webdriver
import allure
import re
from PageObject.Authorization import Authorization
from PageObject.MainPage import MainPage
from PageObject.AdvancedSearch import AdvancedSearch
from config import login, password


@allure.id("ui-1")
@allure.story("UI")
@allure.feature("Авторизация")
@allure.epic("Позитивная")
@allure.title("Проверка авторизации с валидными почтой/логином и паролем")
@allure.description("Проверка авторизации с валидными почтой/логином и паролем")
@allure.severity("blocker")
def test_authorization():
    driver = webdriver.Chrome()
    authorization = Authorization(driver)
    authorization.authorization(login, password)
    driver.quit()


@allure.id("ui-2")
@allure.story("UI")
@allure.feature("Поиск")
@allure.epic("Позитивная")
@allure.title("Проверка поиска фильма в поисковой строке")
@allure.description("Проверка поиска фильма в поисковой строке")
@allure.severity("normal")
def test_search_bar_positive():
    driver = webdriver.Chrome()
    authorization = Authorization(driver)
    authorization.authorization(login, password)
    main_page = MainPage(driver)
    text = main_page.search_bar_positive('след')
    with allure.step("Проверить, что в результате поиска отображен текст 'Возможно, вы искали'"):
        assert text == 'Возможно, вы искали'
    driver.quit()


@allure.id("ui-3")
@allure.story("UI")
@allure.feature("Поиск")
@allure.epic("Негативная")
@allure.title("Проверка поиска несуществующего фильма в поисковой строке")
@allure.description("Проверка поиска несуществующего фильма в поисковой строке")
@allure.severity("normal")
def test_search_bar_negative():
    driver = webdriver.Chrome()
    authorization = Authorization(driver)
    authorization.authorization(login, password)
    main_page = MainPage(driver)
    text = main_page.search_bar_negative('следрерп')
    with allure.step("Проверить, что в результате поиска отображен текст 'По вашему запросу ничего не найдено'"):
        assert text == 'По вашему запросу ничего не найдено'
    driver.quit()


@allure.id("ui-4")
@allure.story("UI")
@allure.feature("Поиск")
@allure.epic("Позитивная")
@allure.title("Проверка расширенного поиска по названию фильма")
@allure.description("Проверка расширенного поиска по названию фильма в блоке 'Искать фильм:'")
@allure.severity("normal")
def test_advanced_search_name_of_film_positive():
    driver = webdriver.Chrome()
    authorization = Authorization(driver)
    authorization.authorization(login, password)
    main_page = MainPage(driver)
    main_page.open_advanced_search()
    advanced_search = AdvancedSearch(driver)
    advanced_search.fill_block_search_for_a_movie_field_name_of_film('след')
    text = advanced_search.click_block_search_for_a_movie_button()
    with allure.step("Проверить, что в результате поиска количество найденных фильмов больше 0"):
        match = re.search(r'результаты: (\d+)', text)
        if match:
            result_count = int(match.group(1))
            assert result_count > 0, f"Число результатов должно быть больше 0, но было {result_count}"
        else:
           raise ValueError("Не удалось извлечь количество результатов из текста")
    driver.quit()


@allure.id("ui-5")
@allure.story("UI")
@allure.feature("Поиск")
@allure.epic("Негативная")
@allure.title("Проверка расширенного поиска по названию несуществующего фильма")
@allure.description("Проверка расширенного поиска по названию несуществующего фильма в блоке 'Искать фильм:'")
@allure.severity("normal")
def test_advanced_search_name_of_film_negative():
    driver = webdriver.Chrome()
    authorization = Authorization(driver)
    authorization.authorization(login, password)
    main_page = MainPage(driver)
    main_page.open_advanced_search()
    advanced_search = AdvancedSearch(driver)
    advanced_search.fill_block_search_for_a_movie_field_name_of_film('следапапа')
    text = advanced_search.click_block_search_for_a_movie_button()
    with allure.step("Проверить, что в результате поиска количество найденных фильмов равно 0"):
        match = re.search(r'результаты: (\d+)', text)
        if match:
            result_count = int(match.group(1))
            assert result_count == 0, f"Число результатов должно быть 0, но было {result_count}"
        else:
            raise ValueError("Не удалось извлечь количество результатов из текста")
    driver.quit()


@allure.id("ui-6")
@allure.story("UI")
@allure.feature("Поиск")
@allure.epic("Позитивная")
@allure.title("Проверка расширенного поиска по жанру фильма")
@allure.description("Проверка расширенного поиска по жанру фильма в блоке 'Искать фильм:'")
@allure.severity("normal")
def test_advanced_search_genre_positive():
    driver = webdriver.Chrome()
    authorization = Authorization(driver)
    authorization.authorization(login, password)
    main_page = MainPage(driver)
    main_page.open_advanced_search()
    advanced_search = AdvancedSearch(driver)
    advanced_search.fill_block_search_for_a_movie_field_genre('биография')
    text = advanced_search.click_block_search_for_a_movie_button()
    with allure.step("Проверить, что в результате поиска количество найденных фильмов больше 0"):
        match = re.search(r'результаты: (\d+)', text)
        if match:
            result_count = int(match.group(1))
            assert result_count > 0, f"Число результатов должно быть больше 0, но было {result_count}"
        else:
            raise ValueError("Не удалось извлечь количество результатов из текста")
    driver.quit()


@allure.id("ui-7")
@allure.story("UI")
@allure.feature("Поиск")
@allure.epic("Позитивная")
@allure.title("Проверка расширенного поиска по по жанру и стране фильма")
@allure.description("Проверка расширенного поиска по жанру и стране фильма в блоке 'Искать фильм:'")
@allure.severity("normal")
def test_advanced_search_genre_and_country_positive():
    driver = webdriver.Chrome()
    authorization = Authorization(driver)
    authorization.authorization(login, password)
    main_page = MainPage(driver)
    main_page.open_advanced_search()
    advanced_search = AdvancedSearch(driver)
    advanced_search.fill_block_search_for_a_movie_field_genre('биография')
    advanced_search.fill_block_search_for_a_movie_field_country('США')
    text = advanced_search.click_block_search_for_a_movie_button()
    with allure.step("Проверить, что в результате поиска количество найденных фильмов больше 0"):
        match = re.search(r'результаты: (\d+)', text)
        if match:
            result_count = int(match.group(1))
            assert result_count > 0, f"Число результатов должно быть больше 0, но было {result_count}"
        else:
            raise ValueError("Не удалось извлечь количество результатов из текста")
    driver.quit()


@allure.id("ui-8")
@allure.story("UI")
@allure.feature("Поиск")
@allure.epic("Позитивная")
@allure.title("Проверка расширенного поиска фильма по создателям")
@allure.description("Проверка расширенного поиска фильма по создателям в блоке 'Искать фильм по создателям:'")
@allure.severity("normal")
def test_advanced_search_by_creators_positive():
    driver = webdriver.Chrome()
    authorization = Authorization(driver)
    authorization.authorization(login, password)
    main_page = MainPage(driver)
    main_page.open_advanced_search()
    advanced_search = AdvancedSearch(driver)
    advanced_search.fill_block_search_for_by_creators_boxs('Режиссер', 'ромащ', 'Игорь Ромащенко')
    text = advanced_search.click_block_search_by_creators_button()
    with allure.step("Проверить, что в результате поиска количество найденных фильмов больше 0"):
        match = re.search(r'результаты: (\d+)', text)
        if match:
            result_count = int(match.group(1))
            assert result_count > 0, f"Число результатов должно быть больше 0, но было {result_count}"
        else:
            raise ValueError("Не удалось извлечь количество результатов из текста")
    driver.quit()