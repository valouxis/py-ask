'''
https://edabit.com/challenge/QN4RMpAnktNvMCWwg
Identity Matrix
---------------
An identity matrix is defined as a square matrix with 1s running 
from the top left of the square to the bottom right. 
The rest are 0s. 

Create a function that takes an integer n and returns 
the identity matrix of n x n dimensions. 
For this challenge, if the integer is negative, return the mirror 
image of the identity matrix of n x n dimensions. 

Examples
id_mtrx(2) ➞ [
  [1, 0],
  [0, 1]
]
id_mtrx(-2) ➞ [
  [0, 1],
  [1, 0]
]
id_mtrx(0) ➞ []

Notes
Incompatible types passed as n should return the string "Error".
'''
def id_mtrx(n):
    if not type(n) is int: return('Error')
    lst = []
    n1 = abs(n)
    for i in range(n1):
        row = [0]*n1
        if n > 0: row[i] = 1 
        else: row[n1-i-1] = 1 
        lst.append(row)
    return lst

print(id_mtrx(2))
print(id_mtrx(-2))
print(id_mtrx(0))
print(id_mtrx('0'))
print(id_mtrx(1.2))
