'''
Mutable 
iterable 
subscriptable 
'''
num = [10,20,30,40]

# print(num)

# * mutable
# num[2] = 150

# * subscriptable
# print(num[0])
# print(num[1])

# * iterable
# for i in num:
#     print(i)


# append 
num.append(50)
print(num)

# extend 
num.extend([50,60,70])
print(num)

# index 
print(num.index(50))


# count 
print(num.count(50))

# insert
num.insert(3, 99)
print(num)


# pop -- index
# num.pop()
num.pop(3)
print(num)

# remove -- element
num.remove(50)
print(num)