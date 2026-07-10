n = int(input("1. Spring\n2. Summer\n3. Monsoon\n4. Winter\nSelect your favourite Season : "))

match n:
    case 1:
        print("Spring is my Favourite Season")
    case 2:
        print("Summer is my Favourite Season")
    case 3:
        print("Monsoon is my Favourite Season")
    case 4:
        print("Winter is my Favourite Season")
    case _ :
        print("Select correct season")
