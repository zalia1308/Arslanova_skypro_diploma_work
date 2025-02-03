import allure
from PageObject.FilmsAPI import FilmsAPI


api = FilmsAPI()


@allure.id("api-1")
@allure.story("API")
@allure.feature("Films")
@allure.epic("Позитивная")
@allure.title("Проверка поиска фильмов по ключевым словам")
@allure.description("Проверка поиска фильмов по ключевым словам с проверкой статус-кода и ответом: количество найденных записей, название, страна, содержание")
@allure.severity("normal")
def test_search_films_by_keywords():
    body = api.get_search_films_by_keywords('зимородок')
    name_ru = body.json()["films"][0]["nameRu"]
    country = body.json()["films"][0]["countries"][0]["country"]
    description = body.json()["films"][0]["description"]
    with allure.step("Проверить, что статус ответа равен 200"):
        assert body.status_code == 200
    with allure.step("Проверить, что в теле ответа количество найденных записей больше 0"):
        assert len(body.json()) > 0
    with allure.step("Проверить, что в теле ответа есть название фильма, которое ищется по ключевому слову"):
        assert name_ru == "Зимородок"
    with allure.step("Проверить, что в теле ответа есть название страны фильма, которое ищется по ключевому слову"):
        assert country == "Турция"
    with allure.step("Проверить, что в теле ответа есть описание фильма, которое ищется по ключевому слову"):
        assert description == "Красавец и ловелас Ферит вырос в богатой семье и привык ни в чём себе не отказывать. Бесконечные вечеринки, новые подружки — вот привычные будни праздного юноши, который не заботится ни о будущем, ни о каких-то достижениях в жизни. Поведение Ферита огорчает его дедушку, уважаемого бизнесмена Халиса Агу. Чтобы обеспечить семью и добиться достойного положения, мужчина тяжело работал и знает цену каждой заработанной монете.\nКогда же в дом Ферита приходит полиция с обыском, Халис Ага понимает, что должен взять судьбу избалованного внука в свои руки. Он решает найти парню достойную невесту из родного города Антепа. Выбор падает на серьёзную красавицу Сейран. Но сможет ли девушка наставить ветреного Ферита на истинный путь?"


@allure.id("api-2")
@allure.story("API")
@allure.feature("Films")
@allure.epic("Позитивная")
@allure.title("Проверка поиска фильмов по различным фильтрам")
@allure.description("Проверка поиска фильмов по различным фильтрам: countries, genres, order, type, rating_from, rating_to, year_from, year_to, page")
@allure.severity("normal")
def test_search_films_by_different_filters():
    order = 'RATING'
    type_film = 'ALL'
    rating_from = 4
    rating_to = 10
    year_from = 2020
    year_to = 2024
    page = 1
    id_countries = api.get_search_id_countries()
    id_genres = api.get_search_id_genres()
    body = api.get_search_films_by_different_filters(id_countries, id_genres, order, type_film, rating_from, rating_to, year_from, year_to, page)
    with allure.step("Проверить, что статус ответа равен 200"):
        assert body.status_code == 200
    with allure.step("Проверить, что в теле ответа количество найденных записей больше 0"):
        assert len(body.json()) > 0


@allure.id("api-3")
@allure.story("API")
@allure.feature("Staff")
@allure.epic("Позитивная")
@allure.title("Проверка поиска информации о составе команды (актера/режиссера/сценариста и т.д.) по фильму")
@allure.description("Проверка поиска информации о составе команды (актера/режиссера/сценариста и т.д.) по id фильма")
@allure.severity("normal")
def test_search_the_composition_of_the_team_by_id_films():
    id_films = api.get_id_films('след')
    body = api.get_search_the_composition_of_the_team_by_id_films(id_films)
    profession_text = []
    for profession in body.json():
     profession_text.append(profession["professionText"])
    with allure.step("Проверить, что статус ответа равен 200"):
        assert body.status_code == 200
    with allure.step("Проверить, что в теле ответа количество найденных записей больше 0"):
        assert len(body.json()) > 0
    with allure.step("Проверить, что в теле ответа есть запись с позицией 'Актеры' в команде"):
        assert "Актеры" in profession_text
    with allure.step("Проверить, что в теле ответа есть запись с позицией 'Режиссеры' в команде"):
        assert "Режиссеры" in profession_text
    with allure.step("Проверить, что в теле ответа есть запись с позицией 'Сценаристы' в команде"):
        assert "Сценаристы" in profession_text
    with allure.step("Проверить, что в теле ответа есть запись с позицией 'Операторы' в команде"):
        assert "Операторы" in profession_text


@allure.id("api-4")
@allure.story("API")
@allure.feature("Staff")
@allure.epic("Позитивная")
@allure.title("Проверка поиска данных по человеку")
@allure.description("Проверка поиска данных по конкретному человеку по id человека")
@allure.severity("normal")
def test_search_information_about_person_by_id_person():
    id_films = api.get_id_films('след')
    id_person = api.get_id_person(id_films)
    body = api.get_search_information_about_person_by_id_person(id_person)
    with allure.step("Проверить, что статус ответа равен 200"):
        assert body.status_code == 200
    with allure.step("Проверить, что в теле ответа количество найденных записей больше 0"):
        assert len(body.json()) > 0


@allure.id("api-5")
@allure.story("API")
@allure.feature("Films")
@allure.epic("Негативная")
@allure.title("Проверка поиска по словам, несуществующего фильма")
@allure.description("Проверка поиска по словам, несуществующего фильма")
@allure.severity("normal")
def test_search_non_existent_films_by_keywords():
    body = api.get_search_films_by_keywords('зиммммм')
    #message = body.json()["message"]       ---Проверка будет включена, когда код статус 404 будет проходить. Сейчас код статус 200 и выдается результат поиска
    with allure.step("Проверить, что статус ответа равен 404"):
       assert body.status_code == 404
    #assert message == "Фильмы не найдены" ---Проверка будет включена, когда код статус 404 будет проходить. Сейчас код статус 200 и выдается результат поиска


@allure.id("api-6")
@allure.story("API")
@allure.feature("Films")
@allure.epic("Негативная")
@allure.title("Проверка поиска фильмов за ненаступивший год")
@allure.description("Проверка поиска фильмов за ненаступивший год")
@allure.severity("normal")
def test_search_films_the_for_year_that_failed():
    order = 'RATING'
    type_film = 'ALL'
    rating_from = 1
    rating_to = 10
    year_from = 2588
    year_to = 3000
    page = 1
    id_countries = api.get_search_id_countries()
    id_genres = api.get_search_id_genres()
    body = api.get_search_films_by_different_filters(id_countries, id_genres, order, type_film, rating_from, rating_to, year_from, year_to, page)
    with allure.step("Проверить, что статус ответа равен 404"):
        assert body.status_code == 404


@allure.id("api-7")
@allure.story("API")
@allure.feature("Staff")
@allure.epic("Негативная")
@allure.title("Проверка поиска актера/режиссера/сценариста и т.д. по несуществующему фильму")
@allure.description("Проверка поиска актера/режиссера/сценариста и т.д. по несуществующему фильму")
@allure.severity("normal")
def test_search_the_composition_of_the_team_by_id_non_existent_films():
    body = api.get_search_the_composition_of_the_team_by_id_films(142)
    with allure.step("Проверить, что статус ответа равен 404"):
        assert body.status_code == 404


# 8 API тест-кейс: Проверка поиска данных по несуществующему человеку   ----негативная
@allure.id("api-8")
@allure.story("API")
@allure.feature("Staff")
@allure.epic("Негативная")
@allure.title("Проверка поиска данных по несуществующему человеку")
@allure.description("Проверка поиска данных по конкретному человеку по несуществующему id человека")
@allure.severity("normal")
def test_search_information_about_person_by_id_non_existent_person():
    body = api.get_search_information_about_person_by_id_person('9954212')
    with allure.step("Проверить, что статус ответа равен 404"):
        assert body.status_code == 404