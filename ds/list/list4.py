'''
* Task 1 : make a list of fruits 
* 1. convert all fruit names to uppercase
* 2. convert all fruits names to lowercase
* 3. remove last fruits from the list 
* 4. add 'Chikoo' in the fruits  

* INPUT : ['Apple','Banana','Mango']
'''
fruits =  ['Apple','Banana','Mango']
uppercase_fruits= []
lowercase_fruits= []
print(fruits)

for fruit in fruits:
    uppercase_fruits.append(fruit.upper())
    lowercase_fruits.append(fruit.lower())

print(uppercase_fruits)
print(lowercase_fruits)

fruits.pop()
print(fruits)

fruits.append("chikoo")
print(fruits)