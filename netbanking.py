#Create netbanking application to transfer balance from one account object to another.
#Create  attributes like balance, pin etc.
#Throw custom exception for Invalid pin and Insufficient balance

class Bank:

    def __init__(self):
        self.__balance=10000
        self.__name=input("Enter Name => ")
        self.__acno=input("Enter Account Number => ")
        self.__pin=input("Enter Pin => ")

    def transfer(self,other):
        pin=input("Enter Pin => ")
        if self.__pin==pin:
            amt=int(input("Enter Amount To Be Transferred => "))
            self.__balance=self.__balance-amt
            other.__balance=other.__balance+amt
            print("Current Balance => ",self.__balance)
            if self.__balance<1000: 
                raise ArithmeticError("Insufficient Balance For Next Transction!!!")
        elif self.__pin!=pin:
                raise ArithmeticError("Incorrect Pin")

def main():
    user1=Bank()
    user2=Bank()

    try:
        user1.transfer(user2)
    except Exception as e:
        print(e)
   
main()
