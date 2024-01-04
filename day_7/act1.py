list_of_values = ["a", "b", "c", "d", "e"]


def function1(values):
    for value in values:
        print(value)


def function2(values):
    print(values[0])
    print(values[1])


def function3(values):
    for x in values:
        for y in values:
            print(x, y)


def function4(values):
    for i in range(4):
        print("Python is great")

    print("Software Engineering is awesome!")
    print("Software Engineering is awesome!")

    for value in values:
        print(value)

    for value in values:
        print(value)


def bonus1(values):
    total = 0
    for i in range(len(values)):
        total += values[i]
    print(total)


def bonus2(a, b):
    count=0
    for i in range(a):
        for j in range(b):
            count += 1
            print(f"Iteration {count}: {i}, {j}")


# It may be helpful to comment out all of the functions beside the function you are focusing on. This can help with determining the output of the function you are analyzing.
if __name__ == "__main__":
    function1(list_of_values)
    function2(list_of_values)
    function3(list_of_values)
    function4(list_of_values)
    bonus1([1,3,7,12,13])
    bonus2(3, 4)
