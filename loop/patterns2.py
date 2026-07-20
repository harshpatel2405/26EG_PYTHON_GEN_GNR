'''
Butterfly Pattern 
 12345678
 *      *   1     6 spaces    n = 4  4 * 2 - i * 2
 **    **   2      4 spaces
 ***  ***   3
 ********   4
 ***  ***
 **    **
 *      *

 parent loop -> number of rows 
    1. left stars    i
    2. space         2 * (n - i)
    3. right stars   i
'''
n = 5
for i in range(1,6): # 1,2,3,4,5
    for j in range(1, i+1):
        print("*", end="")

    for k in range(1, (2*(n-i))+1):
        print(" ", end= "")

    for m in range(1, i+1):
        print("*", end="")
 
    print()
    
for i in range(4, 0, -1): # 1,2,3,4,5
    for j in range(1, i+1):
        print("*", end="")

    for k in range(1, (2*(n-i))+1):
        print(" ", end= "")

    for m in range(1, i+1):
        print("*", end="")
 
    print()
    

# * hollow square 
'''
1 2 3 4
* * * *  1
*     *  2
*     *  3
* * * *  4
'''
print()
print()
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1 or j== n or i == n or i ==1:
            print("* ", end = "")
        else:
            print("  ", end="")

    print()