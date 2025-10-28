# Simple Age Calculator in Python

from datetime import date

# Function to calculate age
def calculate_age(birth_date):
    today = date.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Adjust if current month/day is before the birth month/day
    if days < 0:
        months -= 1
        days += 30  # approximate
    if months < 0:
        years -= 1
        months += 12

    return years, months, days


# Taking user input
print("=== Age Calculator ===")
birth_year = int(input("Enter your birth year (YYYY): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

birth_date = date(birth_year, birth_month, birth_day)

# Calculate and display result
years, months, days = calculate_age(birth_date)
print(f"\nYour Age is: {years} years, {months} months, and {days} days.")
