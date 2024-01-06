# Iterative Binary Search Function          
def binary_search(data, el):
    first = 0
    last = len(data)-1 
    found = False

    while first <= last and not found:
        mid = (first+last)//2

        if data[mid] == el:
            found = True
        else:
            if el < data[mid]: 
                last = mid-1
            else: 
                first = mid+1
    return found

# Recursive Binary Search Function
def recursive_bsearch(data, el):
    if len(data) == 0:
        return False
    else:
        mid = len(data) // 2
        if data[mid] == el:
            return True
        elif el < data[mid]:
            return recursive_bsearch(data[:mid], el)
        else:
            return recursive_bsearch(data[mid+1:], el)


if __name__ == "__main__":
    test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]
    print("Iterative Binary Search")
    print(binary_search(test_list, 12))
    print(binary_search(test_list, 11))
    print("_"* 20)
    print("Recursive Binary Search")
    print(recursive_bsearch(test_list, 12))
    print(recursive_bsearch(test_list, 11))

      