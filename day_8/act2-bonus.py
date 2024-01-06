def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        middle_index = len(lst) // 2
        left = lst[:middle_index]
        right = lst[middle_index:]
        left_partition = merge_sort(left)
        right_partition = merge_sort(right)
        return merge(left_partition, right_partition)


def merge(list1, list2):
    results = []
    while list1 and list2:
        if list1[0] < list2[0]:
            results.append(list1.pop(0))
        else:
            results.append(list2.pop(0))

    return results + list1 + list2


if __name__ == "__main__":
    # Code to test function
    sample_list = [1, 5, 7, 6, 2]
    print(f"Unsorted list: {sample_list}")
    sorted_list = merge_sort(sample_list)
    print(f"Sorted list: {sorted_list}")
    print("_"* 20)
    sample_list = [1, 5, 7, 6, 2, 32, 45,11, 202, 39, 88, 8, 25]
    print(f"Unsorted list: {sample_list}")
    sorted_list = merge_sort(sample_list)
    print(f"Sorted list: {sorted_list}")
    print("_"* 20)

