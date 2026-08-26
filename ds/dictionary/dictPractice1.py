'''
1. Student Marks Management

Create a dictionary containing student names and their marks in 3 subjects.

students = {
    "Harsh": [78, 85, 92],
    "Vasu": [65, 72, 80],
    "Dev": [88, 91, 79],
    "Raj": [55, 68, 74]
}

Perform the following:

Calculate the total and average marks of every student.
Find the student with the highest average.
Find all students whose average is greater than 75.
Store the result in a new dictionary
'''
students = {
    "Harsh": [78, 85, 92],
    "Vasu": [65, 72, 80],
    "Dev": [88, 91, 79],
    "Raj": [55, 68, 74]
}

new_dict = {
    'highest_avg': 0,
    'highest_name': '',

}
marksGreaterThan75names = []
print("Name\tTotal\tAverage")

for name, marks in students.items():
    total = sum(marks)
    avg = total / len(marks)
    print(f"{name}\t{total}\t{avg}")

    if (new_dict['highest_avg'] < avg):
        new_dict['highest_avg'] = avg
        new_dict['highest_name'] = name

    if avg > 75:
        marksGreaterThan75names.append(name)


new_dict["marksGreaterThan75names"] = marksGreaterThan75names
print(new_dict)

'''
<===========================================================================>
2. Product Inventory

Create a dictionary containing product information:

products = {
    "Laptop": (50000, 5),
    "Mouse": (800, 15),
    "Keyboard": (1500, 8),
    "Monitor": (12000, 3)
}

Where the tuple contains:

(price, quantity)

Perform the following:

Calculate the total inventory value of each product.
Find the product with the highest inventory value.
Find products having quantity less than 5.
Store the inventory values in a new dictionary.
'''