import calendar

# Function to display the full year's calendar
def show_full_year_calendar(year):
    print(f"\nFull Calendar for {year}:\n")
    print(calendar.calendar(year))

# Function to display a specific month's calendar
def show_month_calendar(year, month):
    print(f"\nCalendar for {calendar.month_name[month]} {year}:\n")
    print(calendar.month(year, month))

# Function to check if the year is a leap year
def is_leap_year(year):
    if calendar.isleap(year):
        print(f"\n{year} is a leap year.")
    else:
        print(f"\n{year} is not a leap year.")

print("Calendar Module")

# Set the year to 2027
year = 2027

# Display full year calendar
show_full_year_calendar(year)

# Set the month to August (you can change this)
month = 8

# Display the selected month's calendar
show_month_calendar(year, month)

# Check if the year is a leap year
is_leap_year(year)
