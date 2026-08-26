with open("data1.txt",'r') as file:
    line = file.read()
    print(line)
    
with open("data1.txt",'r') as file:
    while True:
        line = file.readline()
        print(file.tell())
        if not line : 
            break
        print(line)
        
with open("data1.txt",'r') as file:
        line = file.readlines()
        print(line)

with open("data1.txt" , 'w') as file:
    file.write("Done with help of with")
    
with open("data1.txt",'r') as file:
    line = file.read()
    print(line)