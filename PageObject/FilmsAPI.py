import requests
import allure
from config import basic_url_1, basic_url_2, basic_url_3, token


class FilmsAPI:
    """
    Этот класс представляет страницу поиска с функциями API поиска
    """
    def __init__(self):
        self.basic_url_1 = basic_url_1
        self.basic_url_2 = basic_url_2
        self.basic_url_3 = basic_url_3
        self.token = token


    @allure.step("Отправить GET запрос на получение списка фильмов по ключевым словам {my_keyword}")
    def get_search_films_by_keywords(self, my_keyword: str) -> requests.models.Response:
        """
        Эта функция получает список фильмов по ключевым словам.
        Список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.
        """
        my_headers = {
            'X-API-KEY': self.token,
            'accept': 'application/json'
        }
        body = {
            'keyword': my_keyword
        }
        resp = requests.get(self.basic_url_2 + '/search-by-keyword', params=body, headers=my_headers)
        return resp


    @allure.step("Отправить GET запрос на получение id стран для использования в другом GET запросе")
    def get_search_id_countries(self) -> requests.models.Response:

        """
        Эта функция получает список id стран для использования в функции get_search_films_by_different_filters (получение списка фильмов по различным фильтрам)
        """
        my_headers = {
            'X-API-KEY': self.token,
            'accept': 'application/json'
        }
        resp = requests.get(self.basic_url_3 + '/filters', headers=my_headers)
        id_countries = resp.json()["countries"][0]["id"]
        return id_countries


    @allure.step("Отправить GET запрос на получение id жанров для использования в другом GET запросе")
    def get_search_id_genres(self) -> requests.models.Response:

        """
        Эта функция получает список id жанров для использования в функции get_search_films_by_different_filters (получение списка фильмов по различным фильтрам)
        """
        my_headers = {
            'X-API-KEY': self.token,
            'accept': 'application/json'
        }
        resp = requests.get(self.basic_url_3 + '/filters', headers=my_headers)
        id_genres = resp.json()["genres"][0]["id"]
        return id_genres


    @allure.step("Отправить GET запрос на получение списка фильмов по различным фильтрам")
    def get_search_films_by_different_filters(self, id_countries, id_genres, order: str, type_film: str, rating_from: int, rating_to: int, year_from: int, year_to: int, page: int) -> requests.models.Response:
        """
        Эта функция получает список фильмов по различным фильтрам.
        Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов. Данный эндпоинт не возращает более 400 фильмов.
        Есть такие фильтры:
        countries: array[integer] - список id стран разделенные запятой. Например countries=1,2,3. На данный момент можно указать не более одной страны.
        genres: array[integer] - список id жанров разделенные запятой. Например genres=1,2,3. На данный момент можно указать не более одного жанра.
        order: string - сортировка (Available values : RATING, NUM_VOTE, YEAR; Default value : RATING)
        type: string - тип фильма (Available values : FILM, TV_SHOW, TV_SERIES, MINI_SERIES, ALL; Default value : ALL)
        ratingFrom: number - минимальный рейтинг (Default value : 0)
        ratingTo: number - максимальный рейтинг (Default value : 10)
        yearFrom: integer - минимальный год (Default value : 1000)
        yearTo: integer - максимальный год (Default value : 3000)
        imdbId: string - imdb id (string)
        keyword: string - ключевое слово, которое встречается в названии фильма (string)
        page: integer - номер страницы (Default value : 1)
        """
        my_headers = {
            'X-API-KEY': self.token,
            'accept': 'application/json'
        }
        body = {
            'countries': id_countries,
            'genres': id_genres,
            'order': order,
            'type': type_film,
            'ratingFrom': rating_from,
            'ratingTo': rating_to,
            'yearFrom': year_from,
            'yearTo': year_to,
            'page': page
        }
        resp = requests.get(self.basic_url_3, params=body, headers=my_headers)
        return resp


    @allure.step("Отправить GET запрос на получение id фильма для использования в другом GET запросе")
    def get_id_films(self, my_keyword: str) -> requests.models.Response:
        """
        Эта функция возвращает id_films.
        Сперва находится список фильмов по ключевым словам, потом сохраняется filmId из ответа для использования в других функциях.
        """
        my_headers = {
            'X-API-KEY': self.token,
            'accept': 'application/json'
        }
        body = {
            'keyword': my_keyword
        }
        resp = requests.get(self.basic_url_2 + '/search-by-keyword', params=body, headers=my_headers)
        id_films = resp.json()["films"][0]["filmId"]
        return id_films


    @allure.step("Отправить GET запрос на получение данных об актерах, режиссерах и т.д. по id фильма {id_films}")
    def get_search_the_composition_of_the_team_by_id_films(self, id_films) -> requests.models.Response:
        """
        Эта функция получает данные об актерах, режиссерах и т.д. по id фильма
        """
        my_headers = {
            'X-API-KEY': self.token,
            'accept': 'application/json'
        }
        body = {
            'filmId': id_films
        }
        resp = requests.get(self.basic_url_1, params=body, headers=my_headers)
        return resp


    @allure.step("Отправить GET запрос на получение id человека для использования в другом GET запросе")
    def get_id_person(self, id_films) -> requests.models.Response:
        """
        Эта функция возвращает id_person.
        Сперва находится список фильмов по ключевым словам, потом сохраняется staffId из ответа для использования в других функциях.
        """
        my_headers = {
            'X-API-KEY': self.token,
            'accept': 'application/json'
        }
        body = {
            'filmId': id_films
        }
        resp = requests.get(self.basic_url_1, params=body, headers=my_headers)
        id_person = resp.json()[0]["staffId"]
        return id_person


    @allure.step("Отправить GET запрос на получение данных о конкретном человеке по id_person {id_person}")
    def get_search_information_about_person_by_id_person(self, id_person) -> requests.models.Response:
        """
        Эта функция получает данные о конкретном человеке по id_person
        """
        my_headers = {
            'X-API-KEY': self.token,
            'accept': 'application/json'
        }
        resp = requests.get(self.basic_url_1 + '/' + str(id_person), headers=my_headers)
        return resp