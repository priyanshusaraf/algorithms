def LinearSearch(lys, element):
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1
print(LinearSearch([1, 3, 6, 4, 3, 9], 4)
