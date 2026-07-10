
# * check whether the number is positive
n = int(input("Enter a number : "))

if n > 0:
    print("Positive")


# * check whether the entered number is even or odd
n = int(input("Enter a number : "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# * check whether the entered number is positive , negative or zero
n = int(input("Enter a number : "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
elif n == 0:  # & else can also be used here
    print("Zero")

# * max from three numbers
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))

if a > b:
    if a > c:
        print("A is max")
    else:
        print("C is max")
else:
    if b > c:
        print("B is max")
    else:
        print("C is max")
