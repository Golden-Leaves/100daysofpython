import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
def main():
    global URL
    response = requests.get(URL)
    empire_webpage = response.text
    soup = BeautifulSoup(empire_webpage, "html.parser")
    all_100_movie_titles = " ".join([f"{movie.getText()}\n" for movie in soup.find_all(name="h3",class_="title")])
    with open ("movies.txt","w", encoding="utf-8") as f:
        f.write(all_100_movie_titles.rstrip())
    print("DEBUG END")
    
    
if __name__ == "__main__":
    main()

