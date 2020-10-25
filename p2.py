'''
https://edabit.com/challenge/Nda8BQHhZSajpnt5z
Common Divisor of List
----------------------
Write a function that returns the greatest common divisor 
of all list elements. 
If the greatest common divisor is 1, return 1.

Examples
GCD([10, 20, 40]) ➞ 10
GCD([1, 2, 3, 100]) ➞ 1
GCD([1024, 192, 2048, 512]) ➞ 64

Notes
    List elements are always greater than 0.
    There is a minimum of two list elements given.
'''
# Euclid's algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# def GCD(lst):
#     if len(lst) > 2:
#         x = gcd(lst[-1], lst[-2])
#         lst = lst[:-2] + [x]
#         return GCD(lst)
#     else:
#         return gcd(lst[0], lst[1])

def GCD(lst):
    while len(lst) > 2:
        x = gcd(lst[-1], lst[-2])
        lst = lst[:-2] + [x]
    return gcd(lst[0], lst[1])

# test
print(GCD([10, 20, 40]))
print(GCD([1, 2, 3, 100]))
print(GCD([1024, 192, 2048, 512]))
