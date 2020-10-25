'''
https://edabit.com/challenge/dy3WWJr34gSGRPLee
Making a Box
------------
Create a function that creates a box based on dimension n.

Examples
make_box(5) ➞ 
#####
#   #
#   #
#   #
#####

make_box(3) ➞ 
###
# #
###

make_box(2) ➞ 
##
##

make_box(1) ➞ 
#

print(make_triangle(7)) -->
      #
     # #
    #   #
   #     #
  #       #
 #         #
#############

print(make_triangle(5)) -->
    #
   # #
  #   #
 #     #
#########

print(make_triangle(1)) -->
#
'''
def make_box(n):
    s1 = n * '#'
    lst = [s1]
    if n > 1:
        s2 = '#' + (n-2) * ' ' + '#'
        # for i in range(n-2): lst.append(s2)
        # lst.append(s1)
        lst += [s2] * (n-2)
        lst += [s1]
    return '\n'.join(lst)

# only odd dimensions (height)
def make_triangle(n):
    lst = [' '*(n-1) + '#']
    for i in range(n-2): 
        lst += [' '*(n-i-2) + '#' + ' '*(2*i+1) + '#']
    if n > 1: lst += ['#'*(2*n-1)]
    return '\n'.join(lst)

# test
print(make_box(7))
print(make_box(5))
print(make_box(1))

print(make_triangle(7))
print(make_triangle(5))
print(make_triangle(1))
