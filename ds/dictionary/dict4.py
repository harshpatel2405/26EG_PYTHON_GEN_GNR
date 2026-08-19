student = {
    "name": "ram",
    "age": 25,
    "address": {
        "pincode": 234566,
        "landmark": 'Above SBI Bank',
        "city": "Patna"
    },
    "marks": [100, 20, 30, 50],
    "hobby": {'cricket', 'football', 'volleyball', 'baseball'}
}

# print(student[address["city"]])
print(student["address"]['city'])

print(student.get('address').get('city'))

students = [
    {
        "name": "ram",
        "age": 25,
        "address": {
            "pincode": 234566,
            "landmark": 'Above SBI Bank',
            "city": "Patna"
        },
        "marks": [100, 20, 30, 50],
        "hobby": {'cricket', 'football', 'volleyball', 'baseball'}
    },
    {
        "name": "ram",
        "age": 25,
        "address": {
            "pincode": 234566,
            "landmark": 'Above SBI Bank',
            "city": "Patna"
        },
        "marks": [100, 20, 30, 50],
        "hobby": {'cricket', 'football', 'volleyball', 'baseball'}
    }, {
        "name": "ram",
        "age": 25,
        "address": {
            "pincode": 234566,
            "landmark": 'Above SBI Bank',
            "city": "Patna"
        },
        "marks": [100, 20, 30, 50],
        "hobby": {'cricket', 'football', 'volleyball', 'baseball'}
    }
]

print(students[0]["address"]["city"])