student = {
    "name": "Harsh",
    "age": 22,
    "marks": 98
}

print(student)

#      dict_name[key]
print(student["name"])
print(student["age"])
print(student["marks"])


# adding key
student['rollNo'] = 101

# updating
student["age"] = 21

#  loop -- key
for key in student:
    print(key, '->', student[key])

# for key,value in student:   # * error
#     print(key,'->',student[key])

# loop
for key, value in student.items():
    print(key, '->', value)

# keys
print("Keys : ", student.keys())

# values
print("Values : ", student.values())

# get
print("Name :", student.get("name"))
