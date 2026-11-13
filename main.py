##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "abdulmaleek859@gmail.com"
PASSWORD = "ggjg pcil jgpt ixcz"

#Get today's date
today = dt.datetime.now()
print(today)
#today_formatted = today.strftime("%A, %B %d, %Y %H:%M:%S")

today_tuple = (today.month, today.day)

#Read birthdays.csv
data = pandas.read_csv("birthdays.csv")

#Convert the birthday data into a dictionary
birthdays_dict = {
    (row["month"], row["day"]): row for (index, row) in data.iterrows()
}
#print(birthdays_dict)

#Check if today matches anyone's birthay
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    #Get the person's name and email
    name = birthday_person["name"]
    email = birthday_person["email"]
    #OR
    #name = birthdays_dict[(11, 13)]["name"]
    #email = birthdays_dict[11, 13]["email"]

    random_letter = random.choice([
        "letter_templates/letter_1.txt",
        "letter_templates/letter_2.txt",
        "letter_templates/letter_3.txt",
    ])

    #Read the selected letter
    with open(random_letter) as letter_file:
        letter_contents = letter_file.read()

    letter_contents= letter_contents.replace("[NAME]", name)

    #Send the birthday email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject: Happy Birthday!\n\n{letter_contents}"
        )
    print(f"Birthday message sent to{name}")

else:
    print("No birthdays today")

