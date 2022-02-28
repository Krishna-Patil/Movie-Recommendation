import requests
import random
import os


class RecommendMovie:
    _SECRET_KEY = os.environ.get('SECRET_KEY')

    def top_250():
        res = requests.get(
            f"https://imdb-api.com/en/API/Top250Movies/{RecommendMovie._SECRET_KEY}")
        random_int = random.randint(0, 249)
        if res.ok:
            movies = res.json()['items']
            print(f"Title: {movies[random_int]['title']}")
            print(f"Rank: {movies[random_int]['rank']}")
            print(f"Year: {movies[random_int]['year']}")
            print(f"IMDB Rating: {movies[random_int]['imDbRating']}")
        else:
            print("Sorry for inconvenience. IMDB server is Down.")

    def most_popular():
        res = requests.get(
            f"https://imdb-api.com/en/API/MostPopularMovies/{RecommendMovie._SECRET_KEY}")
        random_int = 0
        if res.ok:
            movies = res.json()['items']
            random_int = random.randint(0, len(movies)-1)
            print(f"Title: {movies[random_int]['title']}")
            print(f"Rank: {movies[random_int]['rank']}")
            print(f"Year: {movies[random_int]['year']}")
            print(f"IMDB Rating: {movies[random_int]['imDbRating']}")
        else:
            print("Sorry for inconvenience. IMDB server is Down.")

    def box_office_of_all_time():
        res = requests.get(
            f"https://imdb-api.com/en/API/BoxOfficeAllTime/{RecommendMovie._SECRET_KEY}")
        random_int = 0
        if res.ok:
            movies = res.json()['items']
            random_int = random.randint(0, len(movies)-1)
            print(f"Title: {movies[random_int]['title']}")
            print(f"Rank: {movies[random_int]['rank']}")
            print(
                f"Worldwide Life Time Gross: {movies[random_int]['worldwideLifetimeGross']}")
            print(
                f"Domestic Life Time Gross: {movies[random_int]['domesticLifetimeGross']}")
        else:
            print("Sorry for inconvenience. IMDB server is Down.")

    def recommend_movie(self):
        query_list = [
            "Enter 'T' for recommendation from Top 250 Movies",
            "Enter 'M' for recommendation from Most Popular Movies",
            "Enter 'B' for recommendation from Box Office of all time"
        ]
        for query in query_list:
            print(query)
        while True:
            input_ans = input("Select Any of the above: ").upper()
            switch = {
                'T': RecommendMovie.top_250,
                'M': RecommendMovie.most_popular,
                'B': RecommendMovie.box_office_of_all_time,
            }
            try:
                switch[input_ans]()
                break
            except KeyError:
                print("Invalid Input!")


if __name__ == '__main__':
    movie = RecommendMovie()
    movie.recommend_movie()
