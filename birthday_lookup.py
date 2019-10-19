# keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. The interaction should look something like this:
# Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >> Who's birthday do you want to look up?
# Benjamin Franklin
# >> Benjamin Franklin's birthday is 01/17/1706.

import sys

birthday_data = {
    'Albert Einstein' : (3, 14, 1879),
    'Benjamin Franklin' : (1, 17, 1706),
    'Ada Lovelace' : (12, 10, 1815)
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
names_list = sorted(list(birthday_data.keys()))

for j in names_list:
    print(j)

query = input("\n >> Whose birthday do you want to look up?: ").strip().title()
while query not in birthday_data:
    if query == "":
        print("\nGoodbye!")
        sys.exit()
    else:
        query = input("\n  >> Not available. Try another name?: ").strip().title()
else:
    month, day, year = birthday_data[query]
    if month < 10:
        month = "0" + str(month)
    if day < 10:
        day = "0" + str(day)
    input(f"\t >> {query}'s birthday is {month}/{day}/{year}. Press ENTER to exit: ") 