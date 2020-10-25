'''
https://edabit.com/challenge/BfSj2nBc33aCQrbSg
Truncatable Primes
------------------
A left-truncatable prime is a prime number that contains no 0 
digits and, when the first digit is successively removed, 
the result is always prime.

A right-truncatable prime is a prime number that contains no 0 
digits and, when the last digit is successively removed, 
the result is always prime.

Create a function that takes an integer as an argument and:
    If the integer is only a left-truncatable prime, return "left".
    If the integer is only a right-truncatable prime, return "right".
    If the integer is both, return "both".
    Otherwise, return False.

Examples
truncatable(9137) ➞ "left"
# Because 9137, 137, 37 and 7 are all prime.

truncatable(5939) ➞ "right"
# Because 5939, 593, 59 and 5 are all prime.

truncatable(317) ➞ "both"
# Because 317, 17 and 7 are all prime and 317, 31 and 3 are all prime.

truncatable(5) ➞ "both"
# The trivial case of single-digit primes is treated as truncatable 
# from both directions.

truncatable(139) ➞ False
# 1 and 9 are non-prime, so 139 cannot be truncatable from 
# either direction.

truncatable(103) ➞ False
# Because it contains a 0 digit (even though 103 and 3 are primes).
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

def truncatable(n):
    if not is_prime(n): return False
    strn = str(n)

    if '0' in strn: return False

    is_left = True
    for i in range(len(strn)-1):
        if not is_prime(int(strn[i+1:])): 
            is_left = False
            break

    is_right = True
    for i in range(len(strn)-1):
        if not is_prime(int(strn[:i+1])): 
            is_right = False
            break

    if is_left and is_right: return 'both'
    elif is_left: return 'left'
    elif is_right: return 'right'
    else: return False

# test
print(truncatable(9137))
print(truncatable(5939))
print(truncatable(317))
print(truncatable(5))
print(truncatable(139))
print(truncatable(103))
