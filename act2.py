# javaScriptArray = [12, 55, 33, 40, 55, 33, 20, 12]

# print(f"Original Array: {javaScriptArray}")

# new_set = set(javaScriptArray)

# print(f"No duplicates: {new_set}")

# Question 1a: Create a set of your own with at least 3 different elements.

# new_set = {4, 7, 9}

# # Question 1b: Add an item to the set that you just created.
# new_set.add(17)

# # Question 1c: Print the set with the new data that you added to it:
# print(new_set)

# Question 2a: Create a tuple with at least 3 elements inside of it.
# menu = ('fish','chips','beer')

# # Question 2b: Print the tuple you just created.
# print(menu)

#Section 2 - loops:

# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# # Question 3: Use a for loop to iterate through the 'days' list above 
# # and print the days of the week:
# for penguin in days:
#     print(penguin)


# x = 10
# add_list = [10, 6, 12, 4, 5]
# # Question 4: Uncomment the list and variable x above.  
# # Loop through add_list and add each value to x. 
# # Print the value of x at each increment:
# for value in add_list:
#     answer = value + x
#     print(answer)

# print(answer)

# Question 5: While Loops 

#Declare an iterator variable (set to the number 1) and 
# write a While loop that adds 5 to the value of the variable 
# # starting_value as long as the iterator is under 10:
# iterator = 1
# starting_value = 5

# while iterator < 10:
#     starting_value = starting_value + 5
#     print(f"starting_value = {starting_value}")
#     iterator += 1


#Section 3 - conditionals: if, elif, else statements

favorite_movie = "March of Penguins"    
#Question 6a: Uncomment the favorite_movie variable above and change the value to the 
# title of your favorite movie
#Below, write a conditional statement that prints the string 
# "that's a great movie" if the favorite_movie variable equals your favorite movie.
#Otherwise (else), print the string "that's not my favorite movie".  
#Mess around with the value of the favorite_movie variable and trigger 
# both conditional responses:
# if favorite_movie == "Starship Troopers":
#     print("that's a great movie")
# elif favorite_movie.lower() == "starship troopers":
#     print("Check your capitalization")
#     print(favorite_movie)
# else:
#     print("that's not my favorite movie")

#Question 6b: Uncomment the movie_list variable below and implement a for loop that 
# iterates through each item in the list. 
#If the item is a blueberry (or another fruit), print "item is a fruit and not movie"; 
#if the item is a car manufacturing company like Toyota, print "item is a car and not a movie"; 
#otherwise, just print the movie in the list:

movie_list = ["Inception", "blueberries", "Toyota", "Good Will Hunting"]

for element in movie_list:
    if element == "blueberries":
        print("item is a fruit and not movie")
    elif element == "Toyota":
        print("item is a car and not a movie")
    else:
        print(element)




#BONUS - conditional and operators practice:
a = 5
b = 5
c = 12
#Question 7a: Use the correct operator to add variables a & c:
answer = a + c
print(answer)
print(a + c)
#Question 7b: Use the correct operator to subtract variables b & c:
print(f"c - b = {c-b}")

#Question 7c: Use the correct comparison operator that shows 
# if variables a & b equal each other:
print("Version 1: ")
print(True if b == a else False)

print("Version 2:")
if b == a:
    print("True")
else:
    print("False")

#Question 7d: Use the correct operator to find the quotient of variables c & a
print(f" c/a = {c/a}")

#Question 7e: Use the correct operator to find if variables c & b are not equal to each other:
if c != b:
   print("c != b")
else:
    print("c == b") 

print("c != b" if c != b else "c == b")