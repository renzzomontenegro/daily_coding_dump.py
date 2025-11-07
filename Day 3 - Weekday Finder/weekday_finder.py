import calendar

def get_weekday(date_string):
    date_string = date_string.split('-')
    year, month, day = int(date_string[0]), int(date_string[1]), int(date_string[2])
    weekday = calendar.weekday(year, month, day)
    date_string = calendar.day_name[weekday]
    return date_string

while True:
    try:
        date = input(f"\nEnter date (YYYY-MM-DD): ")
        print(get_weekday(date))

    except ValueError:
        print("Invalid Input. Try again.")
        continue