import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""
    list_user = []
    name = ""
    name_id = ""
    st_id = ""
    count = 0
    data_list = []

    def __init__(self, url, id_url, fail):
        self.url = url
        self.fail = fail
        self.id_url = id_url

    def get_html(self):
        req = requests.get(self.url + self.id_url).text
        self.html = BeautifulSoup(req, "lxml")

    def get_id_user(self):
        s = self.html.find(id="main").find_all(class_="row")[2]
        s2 = s.find_all(class_='cl-12 cl-s-3')[3].find(class_='of-auto maxh-800')
        for i in s2:
            try:
                name = i.find('a')["href"]
            except ValueError:
                name = " "
            self.list_user.append(name)

    def get_info_user(self, i):
        self.count += 1
        dannie = []
        soup = self.html.find(id="content").find(class_="row")
        try:
            self.name = soup.find(class_="of-h").find(class_="trim").text

        except ValueError:
            self.name = " "

        try:
            self.st_id = soup.find(class_="of-h").find(target="_blank").text
        except ValueError:
            self.st_id = " "
        try:
            self.data_reg = soup.find(class_="of-h").find_all(class_="pt-5 pb-5")[1].find(class_="f-r ml-5").text
        except ValueError:
            self.data_reg = " "
        self.data_list.append([self.name,self.st_id,self.data_reg])

    def run(self):
        self.get_html()
        self.get_id_user()
        for i in self.list_user:
            self.id_url = i
            if i == " ":
                return " "
            else:
                self.get_html()
                self.get_info_user(i)
        return self.data_list











