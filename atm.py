import random


class Atm:
    def __init__(self, transactionType, balance):
        self.transactionType = transactionType
        self.balance = balance

    def inputValue(self, transactionInput, balanceInput):
        self.transactionType = transactionInput
        self.balance = balanceInput


def main():
    balance = int(random.randint(1000, 9999))
    transactionInput = input("what would you like to do?")
    balanceInput = int(input("how much would you like to"+transactionInput))
    print("your balance was", balance)
    if(transactionInput == "save"):
        balance = balance + balanceInput
    elif(transactionInput == "withdraw"):
        balance = balance - balanceInput
    print(transactionInput, balanceInput)
    print("your balance is", balance)


main()
