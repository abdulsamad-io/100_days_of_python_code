def is_leap_year(year):
    """check if year is leap year"""
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(int(input('Enter year: '))))