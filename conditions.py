import random

def leap_year_quiz():
    response = int(input("How many days are there in a leap year? >>"))
    print("You entered:", response)

    #if response is correct, ask which month as an extra day in leap year    
    #if wrong, end game

if __name__ == '__main__':
    leap_year_quiz()