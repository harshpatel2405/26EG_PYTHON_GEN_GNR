fruits = ['Apple', 'Banana', 'Apple', 'Chikoo', 'Dragon Fruit', 'Fig', 'Guava']
print("Original :", fruits)

# * append
fruits.append('Honey Dew')
print("1. Append :", fruits)

# * extend
newFruits = ['Jack Fruit', 'Kiwi', 'Litchie']
fruits.extend(newFruits)
print(fruits)

# * insert
fruits.insert(3, 'Mango')
print(fruits)

# * pop
fruits.pop()
print(fruits)
fruits.pop(3)
print(fruits)
# fruits.pop(30)# * IndexError: pop index out of range

# * remove
fruits.remove('Apple')
print(fruits)
# fruits.remove('Litchie')#* ValueError: list.remove(x): x not in list

# * sort
fruits.sort()
print(fruits)

# * reverse
fruits.reverse()
print(fruits)

# * count 
print("Count of Apple :",fruits.count('Apple'))

print("Index of Apple :",fruits.index('Apple'))
# print("Index of Apple :",fruits.index('Appl'))# *ValueError: 'Appl' is not in list

# * clear
fruits.clear()
print("Clear :", fruits)

