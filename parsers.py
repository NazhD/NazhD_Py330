import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        new = self.html.find_all("div", class_="caption")
        for item in new:
            title = item.find("h3").text
            href = item.find("a")["href"]
            author = item.find("a", class_="topic-info-author-link").text.strip()
            self.res.append({"title":title ,"href":href, "author":author})


    def save(self):
        with open(self.path, "w") as f:
            i = 1
            for item in self.res:
                f.write(f"Новасть № {i}\n\nНазвание: {item['title']}\nСылка: {item['href']}\nАвтор: "
                        f"{item['author']}\n\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()