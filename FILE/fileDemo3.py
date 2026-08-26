file = open("data1.txt",'r')

#  * will read entire file
# data = file.read()
# print(data)

#  * will read line by line
# data = file.readline()
# print(data)

# while True :
#     data = file.readline()

#     if(not data):
#         break
#     print(data)

# * readlines -- returns list of lines
print(file.readlines())