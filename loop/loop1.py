# * for range


#  * print till 10
#  * range(stop)  (starts from 0 and end stop-1 and increments by 1)

for i in range(11):
    print(i ,end= " ")

for i in range(-5):
    print(i)

print()
# * range(start, stop)  (starts from start, end at stop-1 , increment by 1)
for i in range(1,6):
    print(i, end = " ")

for i in range(5,0):
    print(i)

print()
# * range(start, stop, step ) (starts -> start , stop -> stop-1 , changes by step)
# for i in range(1,7, 1):
#     print(i, end = " ")
# for i in range(1,7, 2):
#     print(i, end = " ")
for i in range(10,-1, -2):
    print(i, end = " ")