'''
https://edabit.com/challenge/GAbxxcsKoLGKtwjRB
Sum of Prime Numbers
--------------------
Create a function that takes a list of numbers and returns 
the sum of all prime numbers in the list.

Examples
sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17
sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87
sum_primes([]) ➞ None

Notes
    List elements are always greater than 0.
    A prime number is a number which has exactly two divisors.
'''
def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def sum_primes(lst):
    plst = []
    for x in lst:
        if is_prime(x):
            plst.append(x)
    
    if len(plst): return sum(plst)
    else: None

# def sum_primes(lst):
# 	isprime = lambda n: n > 1 and all(n % i for i in range(2, int(n**0.5)+1))
# 	return sum(n for n in lst if isprime(n)) or None

# test
print(sum_primes([2]))
print(is_prime(2))

print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_primes([2, 3, 4, 11, 20, 50, 71]))
