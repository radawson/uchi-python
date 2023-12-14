# def inner_funcs(int_param):
#     # inner function definition
#     def minus_five(inner_param):
#         return inner_param - 5
    
#     new_val = minus_five(int_param)

#     return new_val

# def minus_five(int_param):
#        return int_param - 6

# def default_add(a, b="a string"):
#     return a / b

def print_list(*names):
    for name in names:
        print(name)

if __name__ == "__main__":
   
#    print(inner_funcs(8)) 
#    print(minus_five(8))
    # print(default_add(12))
    # print(default_add(12, 24))
    # print("_"*40)
    print_list('anne','trevor','eli','marcus')
    a_list = [1,2,3,4]
    print(a_list)
    print(*a_list)
    print(1,2,3,4,*a_list)