import calendar

def days_until_weekend(date_string):
    date_string = date_string.split("-")
    year, month, day = int(date_string[0]), int(date_string[1]), int(date_string[2])
    week = calendar.weekday(year, month, day)
    date_string = week
    return date_string

while True:
    try:
        date = input(f"\nEnter date (YYYY-MM-DD): ")
        day = days_until_weekend(date)

        if day >= 5:
            print(f"\nIt's the weekend!")
        else:
            day_til = 5 - day
            if day_til == 1:
                print(f"\n{day_til} day until the weekend.")
            else:
                print(f"\n{day_til} days until the weekend.")
    
    except ValueError:
        print(f"\nInvalid Input. Try again.")
        continue