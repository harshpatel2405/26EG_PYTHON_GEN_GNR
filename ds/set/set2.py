num = {10,20}

num.add(30)
num.add(20)
print(num)

num.update([90,89])
print(num)

num.remove(89) # will raise keyerror if element not present
print(num)

num.discard(80)
print(num)

num.pop()
print(num)

num.clear()
print(num)

