def sort_words(input_string):
    words = input_string.split()
    sorted_words = sorted(words, key=lambda word: word.lower())
    return sorted_words


def find_pair(array, target):
    sorted_list = sorted(array)
    left = 0
    right = len(sorted_list) - 1
    while left < right:
        current_sum = sorted_list[left] + sorted_list[right]
        if current_sum == target:
            return sorted_list[left], sorted_list[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return "no pairs sum to the target"


def find_pair2(array, target):
    seen_numbers = set()
    for number in array:
        complement = target - number
        if complement in seen_numbers:
            return complement, number
        seen_numbers.add(number)
    return "no pairs sum to the target"


if __name__ == "__main__":
    words = "I love software engineering"
    print(sort_words(words))
    print("_" * 20)
    print("Version 1:")
    num_list = [5, 10, 4, 7, 6, 2]
    print("find 9")
    print(find_pair(num_list, 9))
    print("find 21")
    print(find_pair(num_list, 21))
    print("_" * 20)
    print("Version 2:")
    print("find 9")
    num_list = [5, 10, 4, 7, 6, 2]
    print(find_pair2(num_list, 9))
    print("find 21")
    print(find_pair2(num_list, 21))
