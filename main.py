import smtplib
import datetime as dt
import random
import pandas

my_email = "baz.angra2@gmail.com"
password = "dmhmicwkfjniuyce"
now = dt.datetime.now()
today = now.day
PLACEHOLDER = "[NAME]"

data = pandas.read_csv("birthdays.csv")
list_of_data = data.to_dict(orient="records")

for each in list_of_data:
    if each["day"] == today:
        random_number = random.choice(range(1, 4))
        with open(f"letter_templates/letter_{random_number}.txt", "r") as random_letter:
            letter_contents = random_letter.read()
            new_letter = letter_contents.replace(PLACEHOLDER, each["name"])
            with open(f"sent_{each["name"]}.txt", mode="w") as file:
                file.write(new_letter)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=each["email"],
                msg=f"Subject:Happy Birthday\n\n{new_letter}"
            )