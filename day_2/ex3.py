def concat(**kwargs):
    print(type(kwargs))
    print(kwargs.items())

    concatted=""
    for value in kwargs.values():
        concatted += value + " "
    return concatted
    # for key, value in kwargs.items():

    #     print(f"Key: {key}, Value: {value}")

if __name__ == "__main__":
    print(concat(a="Writing", b="Python", c="Functions",d="Is", e="Great"))