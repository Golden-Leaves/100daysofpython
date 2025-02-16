from bs4 import BeautifulSoup
import requests
def main():
    response = requests.get("https://news.ycombinator.com/news")
    ycomb_webpage = response.text
    soup = BeautifulSoup(ycomb_webpage, "html.parser")
    articles = soup.select(selector="span.titleline a")
    article_links = []
    article_titles = []
    for article in articles:
        article_link  = article.get("href")
        article_text = article.get_text()
        article_titles.append(article_text)
        article_links.append(article_link)
    points_list = [score.getText() for score in soup.find_all(name="span",class_="score")]
    scores_list = [int(score.split(" ")[0]) for score in points_list]
    highest_score = max(scores_list)
    highest_score_index = scores_list.index(highest_score) + 1
    print(highest_score_index)
    best_article_link = article_links[highest_score_index]
    best_article_text = article_links[highest_score_index]
    print(f"The best article is {best_article_text} with {highest_score} upvotes (link:{best_article_link}).")
    
   

if __name__ == "__main__":
    main()