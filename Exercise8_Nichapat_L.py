Username = input("Username :")
Password = input("Password :")
if Username  == "Ari"  and Password == "123456789":
    print("Welcome Ari")
    print("----- Coffee --- Shop -----")
    print("1. Coffee")
    print("2. Cake")
    Selected = int(input("Select : "))
    if Selected == 1 :
        print("1. Americano")
        print("2. Latte")
        print("3. Cappuccino")
        Selected = int(input("Buy : "))
        if Selected == 1 :
            price = 20
            print("You buy Americano")
        elif Selected == 2 :
            price = 25
            print("You buy Latte")
        elif Selected == 3 :
            price = 30
            print("You buy Cappuccino")
    if Selected == 2 :
        print("1. Black Forest")
        print("2. Strawberry")
        print("3. Chocolate")
        Selected = int(input("Buy : "))
        if Selected == 1 :
            price = 99
            print("You buy Black Forest")
        elif Selected == 2 :
            price = 100
            print("You buy Strawberry Cake")
        elif Selected == 3 :
            price = 120
            print("You buy Chocolate Cake")
    print("Total : ", price," bath")

        