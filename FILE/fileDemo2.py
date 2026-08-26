file = open("data1.txt", 'w')
# file = open("data1.txt", 'a')

# file.write("Namaste\n" + "Hello World\tDuniya\n")
# file.write("\tDuniya\n")

data = ['Tom and Jerry\n', 'Motu and Patlu\n', 'Krishna and Bheem\n']
file.writelines(data)


file.close()
