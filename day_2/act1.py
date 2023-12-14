def arb_args(*args):
    for arg in args:
        print(arg)

def inner_func(num1, num2):
    def nested_func1():
        return num1 + num2
    
    def nested_func2():
        return num1 * num2
    
    result = nested_func1() + nested_func2()
    print(result)

def lunch_lady(name, preference=None):
    if preference is None:
        preference = "Mystery Meat"
    print(name, preference)

def sum_n_product(num1, num2):
    return num1 + num2, num1 * num2

alias_arb_args = arb_args

def arb_mean(*args):
    total = sum(args)
    average = total / len(args)
    print(average)

def arb_longest_string(*strings):
    longest = max(strings, key=len)
    return longest

if __name__ == "__main__":
    arb_args(1, "two", 3, "four", True, 42.00)
    print("_"*40)
    inner_func(2, 3)
    print("_"*40)
    lunch_lady("Anne")
    lunch_lady("Trevor", "Salisbury Steak")
    print("_"*40)
    print(sum_n_product(2, 3))
    print(sum_n_product(2, 3)[0])
    print(sum_n_product(2, 3)[1])
    num1, num2 = sum_n_product(2, 3)
    print(f"{num1} and {num2}")
    print("_"*40)
    alias_arb_args(1, "two", 3, "four", True, 42.00)
    print("_"*40)
    arb_mean(1, 2, 3, 4, 5)
    arb_mean(1, 2, 3, 4, 5, 6)
    print("_"*40)
    arb_longest_string("one", "two", "three", "four", "five", "six", "forty two")
