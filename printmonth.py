month = input("Enter the month('January', ...,'December'): ")
day = input("Enter the start day ('Monday', ..., 'Sunday'): ")
print(month)
print("Mo Tu We Th Fr Sa Su")

if day == "Monday":
    n = 1
elif day == "Tuesday":
    n = 0
elif day == "Wednesday":
    n = -1
elif day == "Thursday":
    n = -2
elif day == "Friday":
    n = -3
elif day == "Saturday":
    n = -4
elif day == "Sunday":
    n = -5
else:
    n = 0

if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    m = 31
elif month == "March" or month == "June" or month == "September" or month == "November": 
    m = 30
else:
    m = 28

for i in range(6):
    for k in range(7):
        if n + k < 1 or n + k > m:
            print("  ", end = ' ')
        else:
            print("%2s" % (n + k), end = ' ')
    print()
    n = n + 7