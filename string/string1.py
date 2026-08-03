str1 = 'Harsh'
str2 = "Vasu"
str3 = '''
This is a string

This is a final line
'''
print(str1)
print(str2)
print(str3)

# * access index wise 
print(str1[2])

# * upper
print(str1.upper())

# * lower
print(str1.lower())

name = "harsh patel,Vasu Patel"

print(name.capitalize())
print(name.title())

print(name.count('a'))
print(name.endswith('el'))

print(name.startswith('harsh'))

print(name.index("h"))


print(name.split())
print(name.split(","))

data = "    Helolo      "
print(data.strip() ,".")
print(data.lstrip(),".")
print(data.rstrip(),".")

print(data.find('o'))
print(data.rfind('o'))

ans = "Hello " + " World"
print(ans) 

# * replace 
print(name.replace("h","X"))
print(name)

# * take a phone number from user and update every even character 
str = input("Enter a phone number : ")
new_data = ""
if(len(str) == 10):
    for i in range(10):
        if(i % 2 == 0):
            new_data += '*'
            continue
        new_data += str[i]
else:
    print("Length should be 10")
print(new_data)