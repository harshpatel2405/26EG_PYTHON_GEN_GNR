# * comprehension
new_list = [x for x in range(1, 6)]
print(new_list)

names = ['vasu', 'dev', 'varun']
upper_name = [name.upper() for name in names]
print(upper_name)


'''
 Count Even and Odd Numbers
    Practice Problem: Given a list of integers, iterate through the items and count how many are even and how many are odd.


Given Input: Numbers: [10, 21, 4, 45, 66, 93, 11]

Expected Output:
Even numbers: 3
Odd numbers: 4
'''

# * if_else
even = [x for x in range(1, 11) if x % 2 == 0]
print(even)


notA = [name for name in names if name.count('a') > 0]
print(notA)

# even_odd = ['even' if x%2 ==0 else 'odd' for x in range(1,11)]
even_odd = [x+5 if x%2 ==0 else x+2 for x in range(1,11)]
print(even_odd)