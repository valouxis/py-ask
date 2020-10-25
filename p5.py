'''
https://edabit.com/challenge/Xkc2iAjwCap2z9N5D
Friday the 13th
---------------
Given the month and year as numbers, return whether that month 
contains a Friday 13th.

Examples
has_friday_13(3, 2020) ➞ True
has_friday_13(10, 2017) ➞ True
has_friday_13(1, 1985) ➞ False

Notes
    January will be given as 1, February as 2, etc ...
    Check Resources for some helpful tutorials on Python's datetime module.
'''
import datetime
def has_friday_13(month, year):
    d = datetime.date(year, month, 13)
    return d.weekday() == 4

# Given the year, return how many months contain a Friday 13th.
def how_many_friday_13(year):
    return [has_friday_13(m, year) for m in range(1, 13)].count(True)

# Given the century, return ...
# def year_max_friday_13(century):
    # return max([(how_many_friday_13(y),y) for y in range(century*100, (century+1)*100)])

# test
print(has_friday_13(3, 2020))
print(has_friday_13(10, 2017))
print(has_friday_13(1, 1985))

print(how_many_friday_13(2020))
print(how_many_friday_13(2017))
print(how_many_friday_13(1986))
