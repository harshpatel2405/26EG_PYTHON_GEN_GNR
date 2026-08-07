for x in range(5):
    print(x, end=" ")

x = [x for x in range(5)]
print(x)


print()
for x in range(5):
    if (x % 2 == 0):
        print(x, end=" ")

x = [x for x in range(5) if x % 2 == 0]
print(x)

print()
for x in range(5):
    if x % 2 != 0:
        print("odd -", x, end=" ")

x = [(f"odd - {x}") for x in range(5) if x%2!=0]
print(x)

x = [(f"EVEN - {x}") if x % 2==0 else(f"ODD - {x}") for x in range(5)]
print(x)