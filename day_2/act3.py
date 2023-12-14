def name_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def all_true(iterable):
    for item in iterable:
        if item == False:
            return False
    return True
    #return all(iterable)

def one_true(iterable):
    return any(iterable)

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

def recursive_deduplicate(string):
    if len(string) < 2:
        return string
    if string[0] == string[1]:
        return recursive_deduplicate(string[1:])
    else:
        return string[0] + recursive_deduplicate(string[1:])

def recursive_reverse(string):
    if len(string) <= 1:
        return string
    else:
        return recursive_reverse(string[1:]) + string[0]


if __name__ == "__main__":
    name_args(name="Doug", age=42, favorite_color="blue")
    print("_" * 40)
    print(all_true([True, True, True]))
    print(all_true([True, False, True]))
    print("_" * 40)
    print(one_true([False, False, False]))
    print(one_true([False, True, False]))
    print("_" * 40)
    print(recursive_factorial(5))
    print("_" * 40)
    print(recursive_deduplicate("aaabbbccc"))
    print(recursive_deduplicate("aaabbbcccddd"))
    print("_" * 40)
    print(recursive_reverse("hello"))

