print("\t\t\tMENU")
print("1.Prime numbers between two intervals")
print("2.Inserting element into  nth position of an array")
print("3.finding the missing number from 1 to 100")
option = int(input("Select an option:"))
while option != 0:
    if option == 1:
        START = int(input("starting limit(input should be an integer value)"))
        END = int(input("ending limit"))
        for i in range(START, END + 1):
            if i > 1:
                for j in range(2, i):
                  if i % j == 0:
                     break
                else:
                 print(i)
        option = int(input("Select an option:"))
    elif option == 2:
        N = int(input("enter the size of the array"))
        ARR1 = []
        ARR2 = []
        for i in range(0, N):
            inp = int(input("Enter the array elements"))
            ARR1 = ARR1 + [inp]
        print("array before insertion", ARR1)
        pos = int(input("enter the position to be inserted"))
        x = int(input("element to be inserted"))
        for j in range(0, N + 1):
            if j < pos:
                ARR2 = ARR2 + [ARR1[j]]
            elif j == pos:
                 ARR2 = ARR2 + [x]
            elif j > pos:
                 ARR2 = ARR2 + [ARR1[j-1]]
        print("array after insertion", ARR2)
        option = int(input("Select an option:"))
    elif option == 3:
        a = [*range(1, 101)]
        Sum = 0
        n = int(input(" enter the element to be deleted:"))
        a[n - 1] = 0
        for i in range(100):
            Sum = Sum + a[i]
        total = int(100*(100+1)/2)
        missing_number = total-Sum
        print("the missing number is:", missing_number)
        option = int(input("Select an option:"))
    else:
        print("invalid option")
        option = int(input("Select an option:"))