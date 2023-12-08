
class FilmData:
    def __init__(self, title, genre, producer, year_of_release, duration, atelier, actors):
        self.title = title
        self.genre = genre
        self.producer = producer
        self.year_of_release = year_of_release
        self.duration = duration
        self.atelier = atelier
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.genre})"


class FilmModel:
    def __init__(self):
        self.film_data = {}

    def add_films(self, film_dict):
        film_file = FilmData(*film_dict.values())
        self.film_data[film_file.title] = film_file

    def get_film_file(self):
        return self.film_data.values()

    def get_selected_film_from_list(self, select):
        get_film = self.film_data[select]
        dict_film = {
            "название": get_film.title,
            "жанр": get_film.genre,
            "режиссер": get_film.producer,
            "год выпуска": get_film.year_of_release,
            "длительность": get_film.duration,
            "студия": get_film.atelier,
            "актеры": get_film.actors
        }
        return dict_film

    def delite_file(self, select):
        del self.film_data[select]





