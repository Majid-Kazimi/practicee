# import math
# import pprint
# from cgitb import reset
import itertools

#  def base_conversion(number, base):
#      if number <= 0:
#          return "0"
#
#      digits_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
#      result = ""
#
#      while number != 0:
#          result = digits_list[number % base] + result
#          number //= base
#
#      return result
#
#  base = (input("Enter the destination base (2 - 9): "))
#  number = int(input("Enter a base 10 number" + ": "))
#  result = base_cenversion(number, base)
#
#
# print(f"The number {number} in base {base} is: {result}")
##################################################################
# def base_conversion(number, base):
#
#
#     result = ""
#     if number <= 0:
#          return "0"
#
#      while number > 0:
#          remainder = number % base
#          result = str(remainder) + result
#          number = number // base
#      return result
#
#
#  def main():
#
#      base = int(input("Enter the destination base (2 - 9): "))
#      number = int(input("Enter a base 10 number" + ": "))
#     result = base_conversion(number, base)
#     print(f"The number {number} in base {base} is: {result}")
#
#
# if __name__ == "__main__":
#     main()
#############################################################################
# def caesercipher(message, encode, shift):
#     result = ""
#
#     if encode == "decode":
#         shift = - shift
#
#     for char in message:
#         if "a" <= char <= "z":
#             shifted = ord(char) + shift
#             if shifted > ord("z"):
#                 shifted -= 26
#             elif shifted < ord("a"):
#                 shifted += 26
#             result += chr(shifted)
#
#         elif "A" <= char <= "Z":
#             shifted = ord(char) + shift
#             if shifted > ord("Z"):
#                 shifted -= 26
#             elif shifted < ord("A"):
#                 shifted += 26
#             result += chr(shifted)
#         else:
#             result += char
#     return result
#
#
# def main():
#     message = input("Enter a message:\n")
#     encode = input("Please enter 'encode' for encoding and 'decode' for"
#                    "'decoding':\n").lower()
#     shift = int(input("Please enter the shift number:\n"))
#     print("Result: ", caesercipher(message, encode, shift))
#
#
# if __name__ == '__main__':
#     main()
#######################################################################
# list = [1, 2 , 0, 5, 8, 2, 6, 10]
# list1 = ["a", "b", "r", "h", "r", "z"]
# list2 = ("a","e", "3", "2", "0", "12")
# print (max(list))
# print (max(list1))
# print (max(list2))
#########################################################################
# def prime(n):
#     numbers = list(range (0, n+1))
#     primes = [True] * (n+1)
#     primes[0] = primes[1] = False
#     p = 2
#     for number in range(p*p, n+1, p):
#         primes[number] = False
#         p += 1
#     for number in range(2, n+1):
#         primes.append[number]
#         p += 1
#     return primes
# def main():
#     n = 30
#     print(prime(n))
# if __name__ == '__main__':
#     main()
#######################################################################
# user = int(input("Enter a number: "))
# if user < 25:
#     car = 4800
# else:
#     car = 2200
# print("annual price: $%d" % car)
#########################################################################
# user = int(input("Enter a number: "))
# if user < 7:
#     print(r"acid \n bad")
#     print("acid \n bad")
#     if user < 3:
#         print("don't")
#     else:
#         print("love")
# print("alkaline")
####################################################################
# x = "adfasASsvasdf ABCD efgh"
#
# y = (".. sds ad fs d"
#      "dfsdd f"
#      "sdfsdfd,,, ")
#
# z = "kddkdf"\
#      "j;dskj;kja"\
#     "m kadmv"
#
# print(x)
# print(y.strip())
# print(y.strip(", . d"))
# print(y.lstrip())
# print(y.rstrip())
# print(x.upper())
# print(x.lower())
# print(x.swapcase())
# print(x.title())
# print(x.isalpha())
# print(x.isnumeric())
# print(x.isdigit())
# print(x.split())
# print(x.split(","))
# print(x.split(" "))
# print(x.join("ABC a, b"))
# print(x.replace("A", "B"))
# print(len(x))
# print(x[0])
# print(x)
#######################################################################
# x = 6
# def f():
#     # print ("Within f: x=", )
#     x = 12
#     print("Within f: x =", x)
#
# print("before f: x=", x)
# f()
#print("After f: x=", x)
#################################################################
# x = [1, 2, 3, 4, 5]
# y = (1, 2, 3, 4, 5)
# print (len(x))
# print (len(y))
# print(x.sort())
# print(y.sort())
###########################################################
# x = list ("hello there")
# print(x)
# x = "hello world"
# print(x, end=".")
# print(x, end=" .")
# age = 25
# print("I\'m", str(age), "years old",end="  .")
# print("good\n by. ",end="")
# print("good by")

#############################################################
# def x (num):
#     if num % 2 ==0:
#         return num
#     else:
#         return num +2
# list = [x(num) for num in range (0, 20, 3)]
# list = list[1:-2]
# print(list)
###########################################################
# print("pi equals {m.pi:.3f}".format(m=math))
###########################################################

# print("%d" % 12.2)
# print("%f" % 12.2)
# apr = 12
# print("Annual percentage rate is %f" % apr)
# print ("Annual percentage rate is %f %%" %apr)
# name = "Siamak"
# print("%s" % name)
# name = "math"
# room = 645
# print("course %s is in %d" % (name, room))
############################################################
# x = 23.34
# y = -23.23
# z = 23, 45, 46, 436, 45, 78 ,546
# print(math.ceil(x))
# print(math.ceil(y))
# print(math.floor(x))
# print(math.floor(y))
# print(math.trunc(x))
# print(math.trunc(y))
# print(math.fabs(x))
# print(math.fabs(y))
# print(math.pow(x,2))
# pprint(x)
############################################################
# x = "abDFg"
# for letter in x:
#     print(letter)
############################################################
# continue_x = True
# while continue_x:
#     print("happy")
#     repeat = input("Continue? (y/n): ")
#     if repeat.strip().lower() == "n":
#         continue_x = False
################################################################
# dic = {"a":1, "b":2, "c":3}
# for name in sorted(dic.keys()):
#     print(name.title(), dic[name])
#     print(name.title() + " like " + str(dic[name]))
################################################################
# for row in range(5):
#     for column in range(5):
#         # print(row, column)
#         # print("Hi")
#         # print(row+column)
#         # print("row" + str(row), "column" + str(column))
#         print("(" + str(row) + "," + str(column) + ")", end=" ")

##############################################################
# n = list (range(-10,300))
# for i in n:
#     print(i,id(i),id(i+1)-id(i))
############################################################
# x= 44
# y = 234
# result = x & y
# result = ~x
# result = x >> 2
# result = y << 2
# result = x | y
# result = x ^ y
#
# print (result)
##########################################################
# m = ["a", "b"]
# y = m
# m[1]="c"
# print(m)
# print(y)
#############################################################
# import random
#
#
# def make_board(rows, columns):
#     """
#     Create the board limits.
#     """
#     board = {}
#     for row in range(rows):
#         for column in range(columns):
#             board[(row, column)] = "Empty room"
#     return board
#
#
# def character():
#     """
#     Define the state of player.
#     """
#     return {"X_coordinate": 0, "Y_coordinate": 0, "Current_HP": 5}
#
#
# def current_location(board, player):
#     """
#     Provide the current location of the player.
#     """
#     location = (player["X_coordinate"], player["Y_coordinate"])
#     print(f"Current location: {location}")
#     return board[location]
#
#
# def player_choice():
#     """
#     Get the player's direction choice.
#     """
#     direction = input(
#         "Which direction would you like to move? Enter 'w' for North, 'd' for East, 's' for South or 'a' for West\n")
#     while direction not in ['w', 's', 'a', 'd']:
#         direction = input("Please choose 'w', 's', 'a', or 'd': ")
#     return direction
#
#
# def move_player(player, direction):
#     """
#     Update player's coordinates based on the direction.
#     """
#     if direction == 'w':  # North
#         player["X_coordinate"] -= 1
#     elif direction == 's':  # South
#         player["X_coordinate"] += 1
#     elif direction == 'a':  # West
#         player["Y_coordinate"] -= 1
#     elif direction == 'd':  # East
#         player["Y_coordinate"] += 1
#
#
# def validate_move(rows, columns, player, direction):
#     """
#     Validate the move to ensure it's within board boundaries.
#     """
#     x, y = player["X_coordinate"], player["Y_coordinate"]
#     if direction == 'w' and x > 0:  # North
#         return True
#     elif direction == 's' and x < rows - 1:  # South
#         return True
#     elif direction == 'a' and y > 0:  # West
#         return True
#     elif direction == 'd' and y < columns - 1:  # East
#         return True
#     else:
#         print("Moved out of bounds. Try a different direction.")
#         return False
#
#
# def guessing_game(player):
#     """
#     Guessing game where the player tries to guess a number between 1 and 5.
#     """
#     foe_choice = random.randint(1, 5)
#     player_guess = int(input("Guess a number between 1 and 5: "))
#
#     if player_guess != foe_choice:
#         print("You guessed wrong. You lost 1 HP!")
#         player["Current_HP"] -= 1
#         print(f"You have {player['Current_HP']} HP left!")
#     else:
#         print("You guessed correctly. Good job!")
#
#
# def achieve_goal(rows, columns, player):
#     """
#     Check if the player achieves the goal by reaching the bottom-right corner.
#     """
#     return player["X_coordinate"] == rows - 1 and player["Y_coordinate"] == columns - 1
#
#
# def check_for_foe():
#     return random.random() < 0.25
#
#
# def still_alive(player):
#     """
#     Check if the player is still alive.
#     """
#     if player["Current_HP"] > 0:
#         return True
#     else:
#         print("Sorry, there is no hope for you. You are dead!")
#         return False
#
#
# def game():
#     rows, columns = 5, 5
#     board = make_board(rows, columns)
#     player = character()
#     achieved_goal = False
#     print("Welcome to the simple game\n")
#
#     while not achieved_goal and still_alive(player):
#         current_location(board, player)
#
#         # Get the player's move direction
#         direction = player_choice()
#
#         # Validate the move
#         if validate_move(rows, columns, player, direction):
#             # Move the player and update location
#             move_player(player, direction)
#             print(f"New location: ({player['X_coordinate']}, {player['Y_coordinate']})")
#
#             # Check for a foe encounter
#             if check_for_foe():
#                 guessing_game(player)
#                 if not still_alive(player):
#                     break
#
#             # Check if the player has achieved the goal
#             achieved_goal = achieve_goal(rows, columns, player)
#         else:
#             print("Please choose a valid move.")
#
#     # End of game messages
#     if achieved_goal:
#         print("Congratulations! You've reached the goal!")
#     else:
#         print("Game over. You've run out of HP!")
#
#
# def main():
#     game()
#
#
# if __name__ == "__main__":
#     main()
########################################################################
# import builtins
# print(dir(builtins))
#
# print(dir(math))
# print(dir())
#####################################################################
# filename = 'programming.txt'
# with open(filename, 'w') as f:
#     f.write("Java is okay.\n")
#     f.write("Python is better!\n")
###################################################################
###################################################################

###################################################################
# def a(base):
#     if base == 0:
#         return
#     else:
#         for x in range(base):
#             print("x", end="")
#         print()
#         a(base-1)
#
# a(6)
####################################################################
# def a (l, to=[]):
#     to.append(l)
#     return to
# def main():
#     m = a(12)
#     print(m)
#
#     my = a(24)
#     print(my)
#
# if __name__ == '__main__':
#     main()
##################################################################
# pairs = []
# names = ("A", "B", "C", "D")
# for pair in zip(itertools.count(1), names):
#     pairs.append(pair)
# print(pairs)
##################################################################
# names = ['maj', 'sam', 'sog', 'reza']
# letter = [len(n) for n in names]
# longest = None
# max_letter = 0
# for name, count in zip(names, letter):
#     if count > max_letter:
#         longest = name
#         max_letter = count
# print(longest)
###################### even number  #####################################
# def even_filter(number):
#     return number % 2 == 0
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(even, data)))

# def odd(number):
#     return number % 2 != 0
# datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(odd, datas)))

# use recursion: ////////////////////
# def even_recursive(num = 2):
#     if num > 10:
#         return
#     print(num, end=', ')
#     even_recursive(num + 2)
# even_recursive()
# print()
# use generator: ////////////////
# def even_generator(num):
#     value = 2
#     while value <= num:
#         yield value
#         value += 2
# for value in even_generator(10):
#     print(value, end=', ')
# print()
# evens = even(12)
# print(next(evens), end=', ')
# print(next(evens), end=', ')
# print(next(evens), end=', ')
# print(next(evens), end=', ')
# print(next(evens), end=', ')
# use itertools  /////////////////
# evens = itertools.count(0, 2)
# even_numbers = []
# for _ in range(5):
#     even_numbers.append(next(evens))
# print(even_numbers)
##################################################################
# def even_items(iterable):
#     for index, value in enumerate(iterable, 1):
#         if index % 2 == 0:
#             print(index, value, end=", ")
# even_items("Christopher Thompson")
#####################################################################
# meals = {'breakfast': 'egg',
# 'lunch': 'poke',
# 'dinner': 'spinach'}
# keys = meals.keys()
# print(keys)
# print(list(keys))
# values = meals.values()
# print(values)
# print(list(values))
# entries = meals.items()
# print(entries)
# print(list(entries))
########################################################################
# def pizza(size, *toppings, sauce=None):
#     if sauce is None:
#         sauce = []  # Default to an empty list if no sauces are provided
#
#     # Create a summary of the pizza order
#     print(f"--- Pizza Order Summary ---")
#     print(f"Size: {size}")
#
#     # Handle toppings
#     if toppings:
#         print("Toppings:")
#         for topping in toppings:
#             print(f"  - {topping}")
#     else:
#         print("No toppings selected.")
#
#     # Handle sauces
#     if sauce:
#         print("Sauces:")
#         for s in sauce:
#             print(f"  - {s}")
#     else:
#         print("No sauces selected.")
#
#     print("---------------------------")
#############################################################################
# def message(times):
#     if times > 0:
#         print("This is my life now.")
#         message(times - 1)
# print(message(2))
#########################################################################
# def factorial(value):
#     if value == 0:
#         return 1
#     else:
#         return value * factorial(value - 1)
# print(factorial(4))
######################################################################
# def print_triangle(base):
#     if base == 0:
#         return
#     else:
#         for x in range(base):
#             print("*", end="")
#         print()
#         print_triangle(base - 1)
# print(print_triangle(5))
######################################################################
# def parent():
#     print("Printing from the parent() function")
#     def first_child():
#         print("Printing from the inner first_child() function")
#     def second_child():
#         print("Printing from the inner second_child() function")
#     second_child()
#     first_child()
# print(parent())
######################################################################
# def english_or_korean(language):
#     def english_version():
#         return "I really like gochujang"
#
#     def korean_version():
#         return "나는 고추장이 좋아"
#
#     if language == "한국어":
#         return korean_version  # Return the function itself
#     else:
#         return english_version  # Return the function itself
#
# # Calling the function
# language = english_or_korean("한국어")  # Returns `korean_version`
# print(language())  # Call the returned function to get its result
#
# language = english_or_korean("English")  # Returns `english_version`
# print(language())  # Call the returned function to get its result
#######################################################################
# nested function:
# def greet(name):
#     # inner function
#     def display_name():
#         print("Hi", name)
#
#     # call inner function
#     display_name()
#
# # call outer function
# greet("John")
######################################################################
# closure function:
# def greet():
#     # variable defined outside the inner function
#     name = "John"
#
#     # return a nested anonymous function
#     return lambda: "Hi " + name
#
# # call the outer function
# message = greet()
#
# # call the inner function
# print(message())
######################################################################
#using closure to print odd numbers:
# def calculate():
#     num = 1
#     def inner_func():
#         nonlocal num
#         num += 2
#         return num
#     return inner_func
#
# # call the outer function
# odd = calculate()
#
# # call the inner function
# print(odd())
# print(odd())
# print(odd())
#
# # call the outer function again
# odd2 = calculate()
# print(odd2())
########################################################################
# def my_decorator(some_other_function_I_am_decorating):
#     def wrapper():
#         print("Something is happening before my function is called.")
#         some_other_function_I_am_decorating()
#         print("Something is happening after my function is called.")
#     return wrapper
# def say_cake():
#     print("Cake! Gâteau! 케이크!, 蛋糕! bánh kem! Торт! केक! کیک 🎂 ")
# say_cake = my_decorator(say_cake)
# print(say_cake())
# # use decorator ##########
# def do_twice(func):
#     def wrapper_do_twice(*args , **kwargs ):
#         func(*args , **kwargs )
#         func(*args , **kwargs )
#     return wrapper_do_twice
# @do_twice
# def say_cake():
#     print("Cake! Gâteau! 케이크!, 蛋糕! bánh ngọt! Торт! केक! کیک 🎂 ")
###################################################################
# def myFun(*argv):
#     for arg in argv:
#         print(arg)
#
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
# extra argument ##################
# def myFun(arg1, *argv):
#     print("First argument :", arg1)
#     for arg in argv:
#         print("Next argument through *argv :", arg)
#
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
####################################################################
# def dec(func):
#     def wrapper(*args, **kwargs):
#         print("something is happening!")
#         return func(*args, **kwargs)
#     return wrapper
#
# @dec
# def greeting(name):
#     return f"Hello {name}"
# print(greeting("Jim"))
#######################################################################
# my_fruity_tuple = ("apple", "banana", "cherry")
# my_fruity_iterator_object = iter(my_fruity_tuple)
# print(next(my_fruity_iterator_object))
# print(next(my_fruity_iterator_object))
# print(next(my_fruity_iterator_object))
# # print(next(my_fruity_iterator_object))     /* what will happen?*/
####################################################################
# choices = []
# boolean_generator = itertools.cycle([True, False])
# for _ in range(10):
#     choices.append(next(boolean_generator))
# print(choices)
#################################################################
# primary_colours = ['cyan', 'magenta', 'yellow']
# permutations = list(itertools.permutations(primary_colours))
# print("There are %d permutations: " % len(permutations))
# for sequence_number, permutation in enumerate(permutations, 1):
#         print("%d:\t%s" % (sequence_number, permutation))
###################################################################
# def mu(numlist):
#     n = len(numlist)
#     if n == 1:
#         return numlist[0]
#     else:
#         temp = mu(numlist[0:n-1])
#         if numlist[n-1] > temp:
#             return numlist[n-1]
#         else:
#             return temp
# def main():
#     number_list = [8, 6, 7, 5, 3, 0, 9, 1, 4, 2]
#     print(mu(number_list))
# if __name__ == "__main__":
#     main()
#######################################################################
# reading = 10
# while reading > 0:
#     if reading % 2 == 0:
#         reading -= 3
#     else:
#         reading -= 1
# print(reading)
######################################################################
# a = [1, 2, 3]  # Create list a
# b = a          # Assign b to reference the same list as a
# c = a.copy()   # Create a shallow copy of a and assign it to c
# b[0] = 5       # Modify the first element of b (and a, since b references a)
# c[1] = 6       # Modify the second element of c (does not affect a)
# result = (a == b, a != c, id(a) == id(b), id(a) != id(c))
#
# # c is a shallow copy of a:
# #
# # a.copy() creates a new list object with the same elements as a but stored in a different memory location.
# # Modifying c[1] = 6 changes only c.
# # After this, c becomes [1, 6, 3].
###################################################################
# import copy
# a = [1, [2, 3], (4, 5, [6, 7])]
# b = a[:]
# c = copy.copy(a)
# d = copy.deepcopy(a)
# a[1][1] = 10
# a[2][2][0] = 11
# # After a[1][1] = 10, the second element of the second item in a is modified.
# # Since b and c share references to the inner list [2, 3], the change affects all three lists.
# # However, after a[2][2][0] = 11, the third element of a is modified. This does not affect b or c because the tuple (4, 5, [6, 7]) is immutable in b and c.
# # Result: a, b, and c are no longer equal.
# # As explained above, d is a deep copy, so it is unaffected by changes to the original list a. After the modifications, d differs from both a and c.
# # Result: a, c, and d are not equal.
# # The second element of b and d are different objects:
# #
# # d is a deep copy, so its second element (a copy of [2, 3]) is independent of the second element in b.
# # The first element of a and b are interned integers:
# #
# # The first element of both a and b is 1, which is an immutable, interned integer in Python.
# # The third element of a and b is the tuple (4, 5, [6, 7]). Tuples are immutable, but the list inside the tuple is mutable. Both a and b share the same reference to the tuple, so they are not different objects.
######################################################################
