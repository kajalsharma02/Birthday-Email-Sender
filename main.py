import random
from datetime import datetime
import pandas
import smtplib

a= datetime.now()
today = (a.month ,a.day)
print(today)

data = pandas.read_csv("C:\\Users\\hp\Documents\\\Python Dev Udemy\\Motivational Quotes Mail\\birthdays.csv")
print(data)

new_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# print(new_dict)

if today in new_dict:
    print("Yes")
    person = new_dict[today]
    with open(f"C:\\Users\\hp\\Documents\\Python Dev Udemy\\Motivational Quotes Mail\\letter_templates\\letter_{random.randint(1,3)}.txt") as f:
        fl = f.read()
        new=fl.replace("[NAME]",person["name"])
        print(new)

        my_email = "kajal.sharma@allen.in"
        password = "bgcb mdoe xdph jull"
        person_email = person["email"]

        connection = smtplib.SMTP("smtp.gmail.com")    
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email, to_addrs=person_email, msg=f"Happy Birthday! \n\n{new}")    
        connection.close()



