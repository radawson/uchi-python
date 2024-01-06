def sort_items(a_list):
    return a_list.sort()

def sorted_items(a_list):
    return sorted(a_list)

if __name__ == "__main__":
    my_list = [3,5,2,1,4]
    print(sorted_items(my_list))
    print(my_list)
    print("_"*20)
    print(sort_items(my_list))
    print(my_list)

    

