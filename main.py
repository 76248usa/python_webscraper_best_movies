from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# anchor_tags = soup.find_all(name="a")
# for tag in anchor_tags:
#     pass
#     #print(tag.getText())
#     #print(tag.get("href"))
# #heading = soup.find(name="h1", id="name")
#
# h3_heading = soup.find_all(name="h3", class_="heading")
# #print(section_heading.get("class"))
# #company_url = soup.select_one(selector="#name")
# headings = soup.select(".heading")
# print(headings)

# response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
# html_text = response.text
# soup = BeautifulSoup(html_text, "html.parser")
# all_movies = soup.find_all(name="h3")
# print(all_movies.reverse())
# movie_titles = [movie.getText() for movie in all_movies]
# print(movie_titles)



import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")









