num = (10,20,30,40,50)

print(num)
print(type(num))

# * subscriptable
print(num[0])

#  * iterable
for i in num:
    print(i)

print(num[7]) # IndexError: tuple index out of range

