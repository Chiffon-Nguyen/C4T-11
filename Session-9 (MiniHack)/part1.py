# ComputerPrice = {
#     'HP': 600,
#     'DELL': 650,
#     'MACBOOK': 12000,
#     'ASUS': 400,
#     'ACER': 350,
#     'TOSHIBA': 600,
#     'FUJITSU': 900,
#     'ALIENWARE': 1000,
# }
# SumofCom = 0
# for keys in ComputerPrice:
#     SumofCom += 1

# print(ComputerPrice['ASUS'])
# inputCom = input("Enter a kind of computer: ")
# if inputCom.upper() in ComputerPrice:
#     print("There are", ComputerPrice[inputCom], "in stock")
# else:
#     print("There's no such a computer")

# sumPurchased = 5*(ComputerPrice['ASUS'])
# print("Your purchase is", sumPurchased)

# comPurchased = input("Enter a name of computer: ").upper()
# numPurchased = int(input("Enter your wished number: "))
# print("Your purchase is",numPurchased*ComputerPrice[comPurchased])
ComputerNum = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30,
}
ComputerNum['TOSHIBA'] = 10
ComputerNum['DELL'] = 10
ComputerNum['MACBOOK'] = 2
ComputerNum['FUJITSU'] = 15
ComputerNum['ALIENWARE'] = 5

Purchased = input("Enter a computer and its number u want to buy, seperated by a ':': ")
listPurchased = Purchased.split(":")
comPurchased = listPurchased[0].upper()
if comPurchased in ComputerNum:
    inStock = ComputerNum[comPurchased] - listPurchased[1]
    print("You buy",listPurchased,comPurchased)
    print("We have", inStock, "more in stock")
else:
    print("We don't have that kind of computer")

