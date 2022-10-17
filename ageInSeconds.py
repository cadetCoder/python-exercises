#Age In Seconds Program exercises

#Stage 1

import datetime as dt

# Get month, date, year of birth
month_birth = int(input("Enter month born (1-1):\t"))
day_birth = int(input("Enter day born (1-31):\t"))
year_birth = int(input("Enter year born (4-digits):\t"))

# Get current month, day, year
current_month = dt.date.today().month
current_day = dt.date.today().day
current_year = dt.date.today().year

# Determine number of seconds in a day, average month and average year
numsecs_day = 24 * 60 * 60
numsecs_year = 365 * numsecs_day

avg_numsecs_year = ((4 * numsecs_year) + numsecs_day) // 4
avg_numsecs_month = avg_numsecs_year // 12

# Calculate approximate age in seconds

numsecs_1900_dob = (year_birth - (1900 * avg_numsecs_year)) + \
                   (month_birth - (1 * avg_numsecs_month)) + \
                   (day_birth * numsecs_day)

numsecs_1900_today = (current_year - 1900 * avg_numsecs_year) + \
                     (current_month - 1 * avg_numsecs_month) + \
                     (current_day * numsecs_day)

age_in_secs = numsecs_1900_today - numsecs_1900_dob

# Getting the current age in year
current_age = current_year - year_birth

# Test output
print("\nThe date of birth read is:\t", month_birth, day_birth,year_birth)

print("The current date read is:\t", current_month, current_day, current_year)
print("\nYou are",current_age,"years old!")
print("\nYou are approximately", age_in_secs,"seconds old")
