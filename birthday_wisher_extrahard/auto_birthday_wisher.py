import smtplib
import pandas
import random
import datetime as dt
def main():
    with open(f"100daysofpython/birthday-wisher-extrahard-start/letter_templates/letter_1.txt") as f:
        letter_1_content = f.read()
    with open(f"100daysofpython/birthday-wisher-extrahard-start/letter_templates/letter_2.txt") as f:
        letter_2_content = f.read()
    with open(f"100daysofpython/birthday-wisher-extrahard-start/letter_templates/letter_3.txt") as f:
        letter_3_content = f.read()
        
    letter_list = [letter_1_content,letter_2_content,letter_3_content]
    birthday_data = pandas.read_csv("100daysofpython/birthday-wisher-extrahard-start/birthdays.csv")
    mom_birthday = birthday_data.iloc[1].to_dict()#Rows start at 0
    dad_birthday = birthday_data.iloc[0].to_dict()
    my_birthday = birthday_data.iloc[2].to_dict()
    people_birthday_list = [mom_birthday,dad_birthday,my_birthday]
    
    sender_mail = "minhtuongle10@gmail.com"
    python_mail_password = "bnpj qcfy pglc pzmz"
    current_datetime = dt.datetime.now()
    current_year = current_datetime.year
    current_month = current_datetime.month
    current_day = current_datetime.day
    current_hour = current_datetime.hour
    
    for person in people_birthday_list:
        if person["month"] == current_month and person["day"] == current_day :
            chosen_email_template = random.choice(letter_list)
            chosen_email_template = chosen_email_template.replace("[NAME]", person["name"])
            with smtplib.SMTP("smtp.gmail.com",port = 587) as connection:
                connection.starttls()
                connection.login(user = sender_mail, password = python_mail_password)
                connection.sendmail(from_addr = sender_mail, to_addrs = person["email"], msg = f"Subject: Happy Birthday!\n\n{chosen_email_template}")
                        
  
if __name__ == "__main__":
    main()