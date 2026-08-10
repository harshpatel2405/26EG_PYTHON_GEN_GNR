names = ('harsh', 'aryan', 'sujal', 'harsh', 'jinendra', 'mansavi', 'sneh')

#  comprehension
num = tuple(x for x in names)
print(num)

#  if_else comprehension
aName = tuple(x for x in names if x.count('a') > 0)
print(aName)


num = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# divFour = tuple("yes" if x % 4 == 0 else 'no' for x in num)
divFour = tuple(x+4 if x % 4 == 0 else x+1 for x in num)
print(divFour)


