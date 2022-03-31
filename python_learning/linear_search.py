

def liner_search(l, target):
    i = 0
    while i < len(l):
        if l[i] == target:
            return i
        else:
            i += 1
    return None


def main():
    l = myList = range(1, 9999999)
    target = 99999999999
    res = liner_search(l, target)
    print(res)

if __name__ == '__main__':
    main()
