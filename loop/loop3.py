# Factors -- numbers which divides the number
# * 12 -> 1,2,3,4,6,12
'''
12 % 1 == 0
12 % 2 == 0
12 % 3 == 0

12 % 12 == 0



'''
# * 28 -> 1,2,4,7,14,28

n = 12
count= 0
for i in range(1,n+1):
    if(n % i == 0):
        print(i, end = "\t")
        count+=1

print("Count :", count)

# * sum and multiplication of factors 