def count_down(n):
    #  Base case
    if n == 0:
        return

    #  Recursive case
    else:
        print(n)
        count_down(n - 1)


# Write a recursive function that prints the natural numbers from 1 to n.
def count_up(limit, current=1):
    #  Base case
    if current > limit:
        return

    #  Recursive case
    else:
        print(current)
        count_up(limit, current + 1)


# Write a function that returns the nth elements in the Fibonacci Sequence.
def fibonacci(n):
    #  Base case
    if n == 0 or n == 1:
        return n

    #  Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Write a recursive function that calculates the value of 'a' to the power of 'b'
def power(a, b):
    #  Base case
    if b == 0:
        return 1

    #  Recursive case
    else:
        return a * power(a, b - 1)


def power_2(a, b):
    return a**b


# Write a function that checks whether a string is a palindrome or not.
# The program should take in a string and return True if the string is a palindrome and False if not.
def is_palindrome(string):
    l_string = string.lower()
    #  Base case
    if len(l_string) <= 1:
        return True

    #  Recursive case
    else:
        return l_string[0] == l_string[-1] and is_palindrome(l_string[1:-1])


# test cases
if __name__ == "__main__":
    n = 8
    count_down(n)
    print("_" * 40)
    count_up(n)
    print("_" * 40)
    print(fibonacci(6))
    print(fibonacci(7))
    print("_" * 40)
    print(power(2, 4))
    print(power_2(2, 4))
    print("_" * 40)
    print(is_palindrome("racecar"))
    print(is_palindrome("dumptruck"))
