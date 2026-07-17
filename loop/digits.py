# * 2568
import math
n = 2568
count = 0
while (n > 0):
    rem = n % 10
    print(rem)

    count += 1
    n = n // 10

print("Count :", count)

# * factorial of digits -- strong number
n = 1454
temp = n
sum = 0
while (n > 0):
    rem = n % 10
    fact = math.factorial(rem)
    sum += fact
    n = n // 10

if (temp == sum):
    print(f"{temp} is strong number")
else:
    print(f"{temp} is not strong number")

# * exponent
for i in range(1, 100001):
    n = i
    temp = n
    sum = 0
    count = 0
    while (n > 0):
        count += 1
        n = n // 10

    n = temp
    while (n > 0):
        rem = n % 10
        exp = math.pow(rem, count)
        sum += exp
        n = n // 10

    if (temp == sum):
        print(f"{temp} is armstrong number")
