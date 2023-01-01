# Problem 1
import time

user_age = int(input("Enter your Age or Year of Birth (yyyy)-"))
current_Year = int(time.strftime("%Y"))


def got_hundred(age):
    if 120 >= age >= 5:
        # if you're 5 or older but 120 or lesser than this will show you results --
        return current_Year+(100 - age)
    elif (current_Year-4) > age >= (current_Year - 120):
        # if you put your birth year --
        # Current year + (100 - your current age) = year you'll become 100
        return current_Year + (100 - (current_Year - user_age))
    elif age == current_Year or age >= (current_Year - 4):
        # if you're messing with me or less than 5 --
        print("You're a newborn or lesser than 5, Go and sleep baby!!")

    elif age > current_Year:
        print("You're not born yet... Stop playing with me !! Enter a valid input...")


def age_detector(year):
    if len(str(year)) == len(str(user_age)):
        output = year - user_age
        if output > 0:
            print(f"At the year of {year}, you'll be {output} years old.")
    elif year > (current_Year - user_age):
        # (current year - age) = Birth year --> now, (specified year - Birth year) = future age...
        output = year - (current_Year - user_age)
        if output > 0:
            print(f"At the year of {year}, you'll be {output} years old.")
    elif year == current_Year - user_age:
        print("It's your Birth year!!")

    elif year < current_Year - user_age:
        print("Sorry i am unable to find you in earth. Maybe You were not here that time!!")


if __name__ == '__main__':
    print(f"You'll be 100 years old at {got_hundred(user_age)}")
    run = True
    while run:
        print("Do you want to get your age at any specified year?")
        asking = input("Enter (y/n) -")
        if asking == "y":
            specific_year = int(input("Enter year of your choice -"))
            age_detector(specific_year)
            if specific_year == user_age:
                print("It's your Birth year!!")
            elif specific_year < user_age:
                print("Sorry i am unable to find you in earth. Maybe You were not in earth that time!!")

        elif asking == "n":
            print("Okay ! Best of Luck!!")
            run = False
