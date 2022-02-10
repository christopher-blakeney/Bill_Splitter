import random

# Defining number of users in 'users' variable

print("Enter the number of friends joining (including you):")

users = int(input())

if users <= 0:

    print("No one is joining for the party")

else:
    print("Enter the name of every friend (including you), each on a new line:")

# Using 'users' variable to define for loop range and adding to dict

    user_names = {}

    for i in range(users):
        user_names[input()] = 0

    print("Enter the total bill value:")

# splitting total bill, rounding to 2 decimals and appending to every key in dict

    total_bill = float(input())

# Declaring who is lucky functionality

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')

    lucky_answer = input()

    if lucky_answer == "Yes":
        lucky_user = random.choice(list(user_names))
        print(lucky_user + " is the lucky one!")

        split_bill_lucky = round(total_bill / (users - 1), 2)

        for i in (user_names):
            if i != lucky_user:
                user_names[i] = split_bill_lucky

        print(user_names)

    else:
        print("No one is going to be lucky")

        split_bill = round(total_bill / users, 2)

        for i in (user_names):
            user_names[i] = split_bill

        print(user_names)



