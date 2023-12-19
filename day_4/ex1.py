# my_dict = dict()
names = ["Alice","Bob","Charlie"]

# for i in names:
# 	my_dict[i] = i.upper()
	
my_dict = {name: name.upper() for name in names }


# my_lst = []
alpha = "abcdefghijklmnopqrstuvwxyz"

# for i in range(10):
# 	my_lst.append(alpha[i])
	

my_lst = [alpha[i] for i in range(10)]

#test = map(lambda num: num *2, range(10))
test = [num *2 for num in range(10)]

unsorted_tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_tuples = sorted(unsorted_tuples, key = lambda x: x[1])

a_list = [3,6,9,2]
cubed_list = lambda x: [i**3 for i in x]

if __name__ == "__main__":
    print(my_dict)
    print(my_lst)
    print(test)
    print(f"Sorted Tuples: {sorted_tuples}")
    print(f"Cubed List: {cubed_list(a_list)}")
