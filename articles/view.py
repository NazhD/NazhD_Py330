def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            get_fanc = func(*args, **kwargs)
            print("=" * 50)
            print()
            return get_fanc
        return wrap
    return wrapper


class UsrInterface:

    @add_title("Редактирование данных")
    def wait_eser_answer(self):
        print("Действия с фильмами:")
        print("1 - Добавление фильмов")
        print("2 - Каталог фильмов")
        print("3 - Просмотр определенного фильма")
        print("4 - Удаление фильма")
        user_answer = input("Выберите вариант действий: ")
        return user_answer

    @add_title("Ввод данных")
    def add_film(self):
        dict_film = {
            "название": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        for key in dict_film:
            dict_film[key] = input(f"Ведите {key} фильма: ")
        return dict_film

    @add_title("Просмотр фильм")
    def display_demo_info(self, film_data):
        for ind, item in enumerate(film_data, start=1):
            print(f"{ind}. {item}".center(50, "="))

    @add_title("Выбор фильма")
    def choose_film_from_list(self):
        choose = input("Какой фильмы вы хотите просмотреть: ")
        return choose

    @add_title("Информация о фильме")
    def render_selected_film(self, selected):
        for key in selected:
            print(f"{key}: {selected[key]}")

    @add_title("Запрос на удаление")
    def del_film_from_data(self):
        choose = input("Какой фильмы вы хотите просмотреть: ")
        return choose

    @add_title("Удаление фильма")
    def file_was_deleted(self,selected):
        print(f"Фильм {selected} был удален из библиотеки.")






