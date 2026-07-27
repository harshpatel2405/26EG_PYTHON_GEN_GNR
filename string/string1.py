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
print(name.replace("ha","X"))
print(name)

