import smtplib
import datetime as dt
import random
def main():
    quotes_list = []
    with open("100daysofpython/quotes.txt","r") as f:
        quotes_list = f.readlines()
    quote_data = (random.choice(quotes_list)).split(" - ")
    quote = quote_data[0]
    quoter = quote_data[1]
    print(quote,quote_data)
    used_gmail_account = "minhtuongle10@gmail.com"
    python_mail_password = "bnpj qcfy pglc pzmz" #App password
    current_time = dt.datetime.now()
    current_day_of_the_week = current_time.day
    if current_day_of_the_week == 1:
        with smtplib.SMTP("smtp.gmail.com", port=587) as gmail_connection:
            gmail_connection.starttls()
            gmail_connection.login(user = used_gmail_account, password = python_mail_password)
            gmail_connection.sendmail(from_addr = used_gmail_account, to_addrs = "letuongminh10@gmail.com", msg = f"Subject: {quoter}\n\n {quote}")
    
if __name__ == "__main__":
    main()