# Import required module
from calendar import calendar

def Year_calendar():
    """This function is used to print the calendar of a given year"""

    Year = int(input("Enter a year --> "))

    print(calendar(Year,3))


if __name__ == "__main__":

    Year_calendar()
    print("Code Completed 🔥")