import requests
import vonage
import os
from dotenv import load_dotenv
from calculate_percentage import calculate_percentage_difference
def main():
    load_dotenv()
    STOCK = "TSLA"
    COMPANY_NAME = "Tesla Inc"
    alphavantage_parameters = {
        "apikey": os.getenv("ALPHAVANTAGE_API_KEY"),
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
    }
    news_api_parameters = {
        "apiKey": os.getenv("NEWS_API_KEY"),
        "q": "tesla",
        "language": "en"
    }
    
    alphavantage_response = requests.get(url = "https://www.alphavantage.co/query", params = alphavantage_parameters)
    alphavantage_response.raise_for_status()
    alphavantage_data = alphavantage_response.json()
    day_keys = list(alphavantage_data['Time Series (Daily)'].keys())


    opening_difference = calculate_percentage_difference(float(alphavantage_data["Time Series (Daily)"][day_keys[1]]["1. open"]),float(alphavantage_data["Time Series (Daily)"][day_keys[0]]["1. open"]))
    stock_data = f"""
    Stock Name: {alphavantage_data["Meta Data"]["2. Symbol"]} ({COMPANY_NAME})
    Last Updated: {alphavantage_data["Meta Data"]["3. Last Refreshed"]}
    Difference: {opening_difference} from {day_keys[1]} to {day_keys[0]}
    """

    
    news_api_response = requests.get(url = "https://newsapi.org/v2/everything?",params =  news_api_parameters)
    news_api_response.raise_for_status()
    news_api_data = news_api_response.json()
    news_articles = news_api_data["articles"]
    selected_news = f"""
    
    Publisher: {news_articles[0]["source"]["name"]}
    Author: {news_articles[0]["author"]}
    Title: {news_articles[0]["title"]}
    Content: {news_articles[0]["description"]}
    URL:  {news_articles[0]["url"]} 
    
    Publisher: {news_articles[1]["source"]["name"]}
    Author: {news_articles[1]["author"]}
    Title: {news_articles[1]["title"]}
    Content: {news_articles[1]["description"]}
    URL:  {news_articles[1]["url"]} 
    
    Publisher: {news_articles[2]["source"]["name"]}
    Author: {news_articles[2]["author"]}
    Title: {news_articles[2]["title"]}
    Content: {news_articles[2]["description"]}
    URL:  {news_articles[2]["url"]} """
    
    sent_message = f"{stock_data}\n\n{selected_news}"
    print(sent_message)
    vonage_headers = {
        "Authorization":  f"Bearer {os.getenv("VONAGE_JWT_TOKEN")}",
        "Content-Type": "application/json"
        
    }
    vonage_payload = {
        "message_type": "text",
        "to": "84966879978",
        "from": "StockInfo",
        "text": sent_message,
        "channel":"sms",
    }
    
    vonage_send = requests.post(url = "https://api.nexmo.com/v1/messages",json = vonage_payload,headers = vonage_headers)
    vonage_send.raise_for_status()

if __name__ == "__main__":
    main()