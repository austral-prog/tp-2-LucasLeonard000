def change():
    expense = 23.75
    money = 100
    change = money - expense
    dollars = int(change)
    cents = int((change - dollars) * 100)
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido:")
    print(money)
    print(f"\nVuelto")
    print(f"\nPesos:")
    print(dollars)
    print("Centavos:")
    print(cents)
