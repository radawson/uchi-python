# Define a function named manyParams() that accepts any number of named parameters. 
# The function should return three lists: a list of all the string parameters, 
# a list of any numerical parameters (each incremented by three), 
# and a list of any non-string and non-numerical parameters.
def manyParams(**kwargs):
    string_params = []
    numerical_params = []
    other_params = []
    
    for key, value in kwargs.items():
        print(f"Processing {key}: {value}")
        if isinstance(value, str):
            string_params.append(value)
        elif isinstance(value, (int, float)):
            numerical_params.append(value + 3)
        else:
            other_params.append(value)
    
    return string_params, numerical_params, other_params

if __name__ == "__main__":
    strings, numbers, other = manyParams(name="Doug", age=42, license=True, favorite_number=7.9, favorite_food="pizza")
    print(f"Strings: {strings}")
    print(f"Numbers: {numbers}")
    print(f"Others: {other}")