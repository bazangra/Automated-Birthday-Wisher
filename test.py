import pandas

data = pandas.read_csv("birthdays.csv")
print(data)
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict[(6, 13)]["name"])


