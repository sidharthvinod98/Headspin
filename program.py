__author__ = "Sidharth Nair"
__email__ = "sidharthvinodkcalicut@gmail.com"

# This program is for the following purposes:

# 1.Prime numbers between two intervals
# 2.Inserting element into  nth position of an array
# 3.finding the missing number from 1 to 100

import constants as cs
import helpers as hp


def menu():
    print("\t\t\tMENU")
    print("1.Prime numbers between two intervals")
    print("2.Inserting element into  nth position of an array")
    print("3.finding the missing number from 1 to 100")

    # Select which program to view by giving option
    option = int(input("Select an option:"))

    if option == 1:
        # finding PRIME numbers between START and STOP
        START = int(input("starting limit(input should be an integer value)"))
        END = int(input("ending limit"))
        primeNumbers = hp.prime(START, END)
        print("Prime Numbers:", primeNumbers)
    elif option == 2:
        # N = size of the array
        N = int(input("enter the size of the array"))
        list = hp.inputHelper(N)
        print("array before insertion", list)
        # pos = position at which new elemnt is to be inserted
        pos = int(input("enter the position to be inserted"))
        # x= new element
        x = int(input("element to be inserted"))
        finalList = hp.insertion(N, list, pos, x)
        print("array after insertion", finalList)
    elif option == 3:
        list = [*range(cs.START, cs.END)]
        # elem = we are deleting and element and a checking whether it is missing in the list
        elem = int(input(" enter the element to be deleted:"))
        missing_number = hp.deleteFromList(elem, list)
        print("the missing number is:", missing_number)
    else:
        print("invalid option")
        return False

    return True


if __name__ == "__main__":
    while True:
        if not menu():
            break
