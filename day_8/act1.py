import time

def bubble_sort(lst):
    for i in range(len(lst) - 1):
        swapped = False
        print(f"Iteration: {i+1}")
        for j in range(len(lst) - 1):
            print(f"\tComparing {lst[j]} and {lst[j + 1]}")
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
                print(f"\t\tSwapped: {lst[j]} and {lst[j + 1]}")
        if not swapped:
            return

    return lst

def get_time(function, list):
    # get the start time
    st = time.process_time()
    result = function(list)
    # get the end time
    et = time.process_time()

    # get the execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
    return result


if __name__ == "__main__":
    # get the start time
    st = time.time()
    sample_list = [1, 5, 2, 6, 7]
    print(f"Unsorted list: {sample_list}")
    bubble_sort(sample_list)
    print(f"Sorted list: {sample_list}")
    # get the end time
    et = time.time()

    # get the execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
    print("_" * 20)
    print("Worst case scenario: reversed list")
    # get the start time
    st = time.time()
    sample_list = [x for x in range(10, 0, -1)]
    print(f"Unsorted list: {sample_list}")
    bubble_sort(sample_list)
    print(f"Sorted list: {sample_list}")
    # get the end time
    et = time.time()

    # get the execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    print("_" * 20)
    print("Best case scenario: sorted list")
    a_list = [x for x in range(1, 11)]
    print(get_time(bubble_sort, a_list))

