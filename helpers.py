__author__ = "Sidharth vinod"
__email__ = "sidharthvinodkcalicut@gmail.com"


# find prime numbers between start and end
def prime(START, END):
    primeNumbers = []
    for i in range(START, END + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primeNumbers.append(i)
    return primeNumbers


# insert an element in a list
def insertion(N, list, pos, x):
    ARR = []
    for j in range(0, N + 1):
        if j < pos:
            ARR = ARR + [list[j]]
        elif j == pos:
            ARR = ARR + [x]
        elif j > pos:
            ARR = ARR + [list[j - 1]]
    return ARR


# delete an element from a list
# n : element to be deleted
# Sum: sum of all elements in list
# total: sum of elements from 1 to 100
def deleteFromList(n, list):
    size = len(list)
    Sum = 0
    list[n - 1] = 0
    for i in range(size):
        Sum = Sum + list[i]
        total = int(size * (size + 1) / 2)
    missing_number = total - Sum
    return missing_number


# returns the list with n number of elements
def inputHelper(N):
    list = []
    for i in range(0, N):
        inp = int(input("Enter the array elements"))
        list = list + [inp]
    return list
