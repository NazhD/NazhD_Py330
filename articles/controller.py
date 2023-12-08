from view import UsrInterface
from models import FilmModel


class Controller:

    def __init__(self):
        self.film_model = FilmModel()
        self.user_interface = UsrInterface()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_eser_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            film_dict = self.user_interface.add_film()
            self.film_model.add_films(film_dict)

        if answer == "2":
            film_data = self.film_model.get_film_file()
            self.user_interface.display_demo_info(film_data)

        if answer == "3":
            select = self.user_interface.choose_film_from_list()
            try:
                choose_data = self.film_model.get_selected_film_from_list(select)
            except KeyError:
                print("Нет данных")
            else:
                self.user_interface.render_selected_film(choose_data)

        if answer == "4":
            request_for_deletion = self.user_interface.del_film_from_data()
            try:
                self.film_model.delite_file(request_for_deletion)
            except KeyError:
                print("Такого фильма в библиотеке нет")
            else:
                self.user_interface.file_was_deleted(request_for_deletion)












