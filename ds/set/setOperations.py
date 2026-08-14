a = {10,20,30,40,50}
b = {30,40,50,60,70}

# * union 
ans = a.union(b)
print(ans)

# * intersection 
ans = a.intersection(b)
print(ans)

# * difference
ans = a - b
print(ans)

# * symmetric difference
ans = a.symmetric_difference(b)
print(ans)  

print(a.isdisjoint(b))
print(a.issubset(b))
print(a.issuperset(b))

# * ask for name and add @gmail.com in the end of each and remove any duplicate elements