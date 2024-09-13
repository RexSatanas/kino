import json
import requests
from settings import headers

url = 'https://api.kinopoisk.dev'


class Kinopoisk:
    @classmethod
    def find_random_film(cls):
        response = requests.get(f'{url}/v1.4/movie/random?notNullFields=name', headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=4, ensure_ascii=False))
            with open('results/random_film.json', 'w', encoding='UTF-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        else:
            print('Ошибка:', response.status_code)

    @classmethod
    def find_movie_by_id(cls, movie_id):
        response = requests.get(f'{url}/v1.4/movie/{movie_id}', headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=4, ensure_ascii=False))
            with open('results/movie_by_id.json', 'w', encoding='UTF-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

        else:
            print('Ошибка:', response.status_code)

    @classmethod
    def find_season(cls):
        response = requests.get(
            f'{url}/v1.4/season?page=1&limit=10&selectFields=&notNullFields=name',
            headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=4, ensure_ascii=False))
            with open('results/season.json', 'w', encoding='UTF-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        else:
            print('Ошибка:', response.status_code)

    @classmethod
    def find_review_by_id(cls, movie_id):
        response = requests.get(f'{url}/v1.4/review?page=1&limit=10&movieId={movie_id}', headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=4, ensure_ascii=False))
            with open('results/reviews.json', 'w', encoding='UTF-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        else:
            print('Ошибка:', response.status_code)


if __name__ == '__main__':
    kinopoisk = Kinopoisk()
    while True:
        print('Выберите нужный вариант:'
              '\n1 - Получить рандомный фильм из базы'
              '\n2 - Найти фильм по id'
              '\n3 - Найти сезон'
              '\n4 - Найти отзывы'
              '\n0 - Выход')
        answer = int(input())

        if answer == 1:
            kinopoisk.find_random_film()
        elif answer == 2:
            film_id = int(input('Введите id фильма: '))
            kinopoisk.find_movie_by_id(film_id)
        elif answer == 3:
            kinopoisk.find_season()
        elif answer == 4:
            film_id = int(input('Введите id фильма: '))
            kinopoisk.find_review_by_id(film_id)
        elif answer == 0:
            print('Завершение работы')
            break
        else:
            print("Выберете вариант из списка")
