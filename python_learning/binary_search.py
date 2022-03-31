
def binary_search_True_False(myList, target):
    if not myList:
        return False
    midPoint = len(myList)//2

    if myList[midPoint] == target:
        return True
    elif myList[midPoint] > target:
        myList = myList[:midPoint-1]
        return binary_search_True_False(myList, target)
    else:
        myList = myList[midPoint + 1:]
        return binary_search_True_False(myList, target)


def binary_search(myList, target):
    first = 0
    last = len(myList)

    while last <= len(myList):
        midPoint = (last + first) // 2
        if myList[midPoint] == target:
            return midPoint
        if myList[midPoint] > target:
            last = midPoint - 1
        else:
            first = midPoint + 1
    return None


def main():
    myList = range(1, 999999999999999)
    target = 999999999999998
    res = binary_search(myList, target)
    print(res)


if __name__ == '__main__':
    main()