# import requests
# import os
# from bs4 import BeautifulSoup
#
#
# class Parser:
#     html = ""
#     list_user = []
#     name = ""
#     name_id = ""
#     st_id = ""
#     count = 0
#
#     def __init__(self, url, id_url, fail):
#         self.url = url
#         self.fail = fail
#         self.id_url = id_url
#
#     def get_html(self):
#         req = requests.get(self.url + self.id_url).text
#         self.html = BeautifulSoup(req, "lxml")
#
#     def get_id_user(self):
#         s = self.html.find(id="main").find_all(class_="row")[2]
#         s2 = s.find_all(class_='cl-12 cl-s-3')[3].find(class_='of-auto maxh-800')
#         for i in s2:
#             try:
#                 name = i.find('a')["href"]
#             except ValueError:
#                 name = " "
#             self.list_user.append(name)
#
#     def get_info_user(self):
#         soup = self.html.find(id="content").find(class_="row")
#         try:
#             self.name = soup.find(class_="of-h").find(class_="trim").text
#         except ValueError:
#             self.name = " "
#         try:
#             self.name_id = soup.find(class_="of-h").find(class_="f-r ml-5").text
#         except ValueError:
#             self.name_id = " "
#         try:
#             self.st_id = soup.find(class_="of-h").find(target="_blank").text
#         except ValueError:
#             self.st_id = " "
#         self.count += 1
#
#     def pr_info(self):
#         print(f"Данные пользователя: № {self.count}")
#         print(f"Имя: {self.name}")
#         print(f"Id: {self.name_id}")
#         print(f"SteamId: {self.st_id}")
#         print()
#
#     def write_info_user(self):
#         with open(self.fail, "a") as f:
#             f.write(f"Данные: № {self.count}\n")
#             f.write(f"Имя: {self.name}\n")
#             f.write(f"Id: {self.name_id}\n")
#             f.write(f"SteamId: {self.st_id}\n")
#             f.write("\n")
#
#     def del_file(self):
#         print(f"По адресу {os.path.abspath(f'{self.fail}')} создан фаил.")
#         print(f"Удалить: нажмите 1.\nОставить: любая другая клавиша")
#         file_delite = input("=>> ")
#         if file_delite == "1":
#             os.remove(self.fail)
#
#     def run(self):
#         self.get_html()
#         self.get_id_user()
#         for i in self.list_user:
#             self.id_url = i
#             if i == " ":
#                 print("нету")
#             else:
#                 self.get_html()
#                 self.get_info_user()
#             self.pr_info()
#             self.write_info_user()
#         self.del_file()








