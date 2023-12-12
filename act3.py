# Function Definition Practice:
# Define functions according to the following prompts. Run the Replit to verify correct output.


# 1. Function that accepts no arguments. It's called say_hello and returns nothing, just prints 'hello'.
def say_hello():
    print("Hello")
    print(__name__)


# 2. a 'sum' function that accepts two integers and returns the sum.
def sum(int1, int2):
    return int1 + int2


# 3. an 'average' function that accepts two numbers and returns the average.
def average(num1, num2):
    return (num1 + num2) / 2


# 4. A function that accepts a first name and a last name and formats it to "{last_name}, {first_name}" (returns a string).
def full_name(first_name, last_name):
    return f"{last_name.capitalize()}, {first_name.capitalize()}"


def name(first_name, last_name):
    return last_name + ", " + first_name


# 5. A function that accepts a first name, last name, graduation year, and student number
# and returns those four items together in a list.
def grad_list(first_name, last_name, grad_year, student_num):
    return [first_name, last_name, grad_year, student_num]


# 6. A function that accepts an integer and returns whether it is above 18 or not (Boolean).
def more_than_18(value):
    if value > 18:
        return True
    else:
        return False


def more(num1):
    return num1 > 10


# 7. A function that accepts a string and prints the string in reverse (no return value).
def reverser(string_in):
    return string_in[::-1]


def reversify(str):
    str1 = ""
    for i in str:
        str1 = i + str1
    return str1


if __name__ == "__main__":
    # say_hello()
    # print(sum(3,4))
    # print(average(4,6))
    # print(full_name("Ronald", "reagan"))
    # print(name("Ronald", "reagan"))
    # print(grad_list("Benjamin", "Franklin", 1747, 4.65))
    # print(grad_list("Benjamin", "Franklin", "1747", "4.65"))
    # print(more_than_18(12))
    # print(more_than_18(42))
    print(reversify("palidrome"))
