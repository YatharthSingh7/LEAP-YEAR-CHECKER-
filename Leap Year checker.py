def is_leap_year(year):
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False

# Test the function
while True:
    try:
        year = int(input("Enter a year: "))
        if year < 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if is_leap_year(year):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
