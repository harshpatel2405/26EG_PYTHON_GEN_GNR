def addition(*args):
    print("Number of args passed by user : ", len(args), end="\t")
    print("Sum : ", sum(args))


addition(10)
addition(10, 20)
addition(10, 20, 30)


def getUserInformation(**kwargs):
    print(kwargs)


getUserInformation(name="harsh", age=22)


def welcome(name = 'user'):
    print("Hello,",name)

welcome()
welcome("harsh")