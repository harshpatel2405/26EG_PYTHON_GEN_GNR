name = 'Harsh'

for i in name:
    print(i, end=", ")

print()
for i in range(len(name)):
    print(name[i], end=", ")

# #################################
n =12

for i in range(1, 11):  # *  this will run from 1 to 10 (11 - 1)
    print(f"{n} * {i} = {n * i}")
    # print(n, "*", i, "=", n*i)

# *  find exponent : base and power (without using **)
# * 2 power 3 = 8

base = 2
power = 3
ans = 1
for i in range(power):
    ans *= base
print(ans)

# * reverse the string using loop 
str = 'Hello World'
reversed_str = ''


for i in range(len(str)-1, -1, -1):
    reversed_str += str[i]

print(reversed_str)
