#arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
    for arg in args:
        print(arg)


# inner_func - Takes in two integers. 
# Two nested functions should perform separate, distinct math operations using the integers. 
# The result of both nested functions should then be added together and printed.
def inner_func(num1, num2):
    def nested_func1():
        return num1 + num2

    def nested_func2():
        return num1 * num2

    result = nested_func1() + nested_func2()
    print(result)


# lunch_lady - Takes in two strings: a student's name and their lunch preference. 
# The function should print both strings. 
# If a lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady(name, preference=None):
    if preference is None:
        preference = "Mystery Meat"
    print(name, preference)


# sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(num1, num2):
    #return num1 + num2, num1 * num2
    ret_sum = num1 + num2
    ret_prod = num1 * num2
    return ret_sum, ret_prod


# alias_arb_args - Should be arb_args but assigned an alias.
alias_arb_args = arb_args


# arb_mean - Accepts any number of integers and prints their average.
def arb_mean(*args):
    total = sum(args)
    average = total / len(args)
    print(average)


# arb_longest_string - Accepts any number of strings and returns the longest one.
def arb_longest_string(*strings):
    longest = max(strings, key=len)
    return longest


if __name__ == "__main__":
    arb_args(1, "two", 3, "four", True, 42.00)
    print("_" * 40)
    inner_func(2, 3)
    print("_" * 40)
    lunch_lady("Anne")
    lunch_lady("Trevor", "Salisbury Steak")
    print("_" * 40)
    print(sum_n_product(2, 3))
    print(sum_n_product(2, 3)[0])
    print(sum_n_product(2, 3)[1])
    num1, num2 = sum_n_product(2, 3)
    print(f"{num1} and {num2}")
    print("_" * 40)
    alias_arb_args(1, "two", 3, "four", True, 42.00)
    print("_" * 40)
    arb_mean(1, 2, 3, 4, 5)
    arb_mean(1, 2, 3, 4, 5, 6)
    print("_" * 40)
    print(arb_longest_string("one", "two", "three", "four", "five", "six", "forty two"))
