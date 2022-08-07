from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass

class Parser:
    def __init__(self, url):
        self.url = url
        self.article_lst = []
    
    def parse(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "lxml")
        films = soup.find("div", class_="ratings_list movieList grid_cell9").findAll("div", class_="movieList_item movieItem movieItem-rating movieItem-position")
        for film in films:
            title = film.find("a", class_="movieItem_title").text
            image_url = film.find("img").get("src")
            abstract = film.find("div", class_="movieItem_details").find("span", class_="movieItem_genres").text + ", " + film.find("div", class_="movieItem_details").find("span", class_="movieItem_year").text
            self.article_lst.append(Article(title, image_url, abstract))
        return self.article_lst
    
@dataclass
class Article:
    title : str
    image_url : str
    abstract : str
