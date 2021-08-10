# # print("Hello World")
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|\n")
# print("|___|")
# character_name = "Tom"
# character_age = 50.23153
# is_male = True
# print("There once was a man named " + character_name + ",")
# print("he was ", character_age, " years old. ", sep = "")
# character_name = "Mike"
# print("He really liked the name " + character_name + ",")
# print("but didn't like being ", character_age, ".", sep = "")
# phrase = "Giraffe Academy"
# # print(phrase + " is cool")
# # print(phrase.lower())
# # print(phrase.upper())
# # print(phrase.upper().isupper())
# # print(phrase.isalpha())
# # print(len(phrase))
# # print(phrase[2])
# # print(phrase[0])
# # print(phrase.index("G"))
# print(phrase.index("Aca"))
# print("Giraffe\nAcademy")
# print(-2.3523523)
# print(3 + 5 + 2 - 4 - 19)
# print(4*6.73 + 2/7/2/3 + 19 - 20)
# print(10 % 3) # modulus: gives us the remainder (answer is 1)
# my_num = 5
# print(my_num)
# print(str(my_num) + " This is my_num")
# print(abs(my_num))
# print(pow(4, 6))
# print(max(1, 5, 7, 2, 93))
# print(min(5, 2, 5, 22, 123, 12, 75, 3, 0))
# print(round(3.62323))
# from math import *
# print(floor(3.7))
# print(ceil(2.2))
# print(sqrt(64323156))
# name = input("Enter your name: ")
# print("Hello " + name)
# age = input("Enter your age: ")
# # print("Hello " + name + ". You are " + age + ".")
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# # result = int(num1) + int(num2)
# result = float(num1) + float(num2)
# print(result)
# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celeb = input("Enter a celebrity: ")
# color = str.lower(color)
# plural_noun = str.capitalize(plural_noun)
# celeb = celeb.capitalize()
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celeb)
# friends_name = ["Ryan", "Mike", "Sarah", "Karen", "Jim"]
# print(friends_name)
# friends_name[0] = "Paul"
# print(friends_name[0])
# print(friends_name[-2])
# print(friends_name[1:4])
# friends_name.extend([3, 2, 6, 2])
# lucky_numbers = [23, 54, 22, 99, 94, 58]
# friends_name.extend(lucky_numbers)
# friends_name.append("Kevin")
# friends_name.insert(1, "Kelly")
# print(friends_name)
# friends_name.remove("Kelly")
# print(friends_name)
# del friends_name[3]
# print(friends_name)
# friends_name.pop()
# print(friends_name)
# print(friends_name.index("Paul"))
# print(friends_name.count("Paul"))
# lucky_numbers.sort()
# lucky_numbers.reverse()
# print(lucky_numbers)
# friends_name.clear()
# print(friends_name)
# lucky_numbers2 = lucky_numbers.copy()
# print(lucky_numbers2)
# tuple1 = (2, 3)
# tuple2 = (5, 2, 5, 29, 43, 55, 2, 18)
# coordinates = [(4, 5), (1, 5), (7, 2), (8, 7)] # you can make lists that contain tuples <--
# print(tuple1)
# print(tuple2[5])
# tuple2[4] = 7
# def say_hi(name, age):
#     print("Hello " + name + ", you are " + str(age))
# say_hi("Mike", 35)
# say_hi("Bob", 44)
# name = input("What's your name? ")
# age = int(input("What's your age? "))
# say_hi(name, age)
# def cubed(num):
#     return float(num ** 3)
# # cubed(4)
# answer = cubed(8)
# print(cubed(4))
# print(answer)

# is_male = True
# if is_male:
#     print("I am a dude.")
# else:
#     print("You aren't a dude.")
#
# is_tall = True
# if is_male and is_tall:
#     print("Play basketball.")
# elif is_male and not(is_tall):
#     print("You're not a tall guy.")
# elif not(is_male) and is_tall:
#     print("You are a tall girl.")
# else:
#     print("You are not a tall girl.")
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3 and "dog" == "dog":
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# print(max_num(33, 40, 500))
# num1 = float(input("Enter a number: "))
# op = input("Enter operation: ")
# num2 = float(input("Enter another number: "))
# if op == "+":
#     print(num1 + num2)
# elif op == ("-"):
#     print(num1 - num2)
# elif op == ("*" or "x"):
#     print(num1 * num2)
# elif op == ("/"):
#     print(num1 / num2)
# else:
#     print("Error. Invalid operator. Please refresh.")
# month_conv = {
#     "Jan" : "January",
#     "Feb" : "February",
#     "Mar" : "March",
#     "Apr" : "April",
#     "May" : "May",
#     "Jun" : "June",
#     "Jul" : "July",
#     "Aug" : "August",
#     "Sep" : "September",
#     "Oct" : "October",
#     "Nov" : "November",
#     "Dec" : "December",
#
# }
# print(month_conv["Nov"])
# print(month_conv.get("Dec", "Not valid"))

# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# print("Done with loop.")
# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# while guess != secret_word and out_of_guesses == False:
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# # while guess != secret_word and guess_count < guess_limit:
# #     guess = input("Enter guess: ")
# #     guess_count += 1
# if out_of_guesses:
#     print("You are out of guesses.")
# else:
#     print("You got the secret word.")
# create game where user has to guess secret word within 3 tries. game will stop after 3 failed attempts.
# secret_word = "bear"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# while guess != secret_word and out_of_guesses == False:
#     if guess_count < guess_limit:
#         guess = input("Guess an animal: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# while guess != secret_word and guess_count != guess_limit:
#     guess = input("Guess an animal again: ")
#     guess_count += 1
# if out_of_guesses:
#     print("You are out of guesses.")
# else:
#     print("Bear is correct.")
# secret_word = cow
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# while guess != secret_word and out_of_guesses == False:
#     if guess_count < guess_limit:
#         guess = input("Guess an animal: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# while guess != secret_word and guess_count < guess_limit:
#     guess = input("Guess another animal: ")
#     guess_count += 1
# if out_of_guesses:
#     print("You are out of guesses.")
# else:
#     print("You guessed bear correctly!")
# x = 5
# while x == 6:
#     print("X is 6.")
# else:
#     print("X is not 6.")
# secret = "road"
# guess = ""
# guess_count = 0
# while guess != secret and guess_count <= 3:
#     if guess_count < 3:
#         guess = input("Enter a guess. ")
#         guess_count += 1
#     else:
#         print("Out of guesses.")
#         guess_count += 1
# while guess == secret and guess_count <= 3:
#         print("You got it.")
#         guess_count += 3
# secret = "bike"
# guess = ""
# guess_count = 0
# while guess != secret and guess_count < 3:
#     guess = input("Guess a word: ")
#     guess_count += 1
#     if guess == secret:
#       print("You got it!")
#       guess_count += 3
#     # else:
#          # print("Guess again: ")
# if guess_count >= 3:
#     print("Out of guesses.")
friends = ["Jim", "Karen", "Sally", "John", "Mike"]
# for letter in "Giraffe Academy":
#     print(letter)
# for number in "Giraffe Academy":
#     print(number)
# for name in friends:
#     print(name)
# for index in range(10):
#     print(index)
# for index in range(3, 7):
#     print(index)
# print(len(friends))
# for index in range(len(friends)):
#     print(friends[index])
#     print(len(friends[index]))
# for index in range(5):
#     if index == 0:
#         print("First iteration")
#     else:
#         print("Not first")
# print(2**3)

# def raise_to_power(base_num, power):
#     result = 1
#     for index in range(power):
#         result = result * base_num
#     return result
# print(raise_to_power(3, 5))
# num_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# print(num_grid)
# print(num_grid[0][2])
# for row in num_grid:
#     for col in row:
#         print(col)
# Giraffe Language: vowels --> g
# dog --> dgg
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
# print(translate(input("Enter a phrase: ")))
# print("Comments are fun")
'''<-- Comments can also be left with triple quote marks -->'''
# try:
#     number = int(input("Enter a number: "))
#     print(number)
#     value = 10 / 0
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid Input")
# employee_file = open("employees.txt", "r")
# print(employee_file.readable())
# print(employee_file.readline())
# for employee in employee_file.readlines():
    # print(employee)
# print(employee_file.read())
# employee_file.close()
# employee_file = open("employees2.txt", "w")
# employee_file.write("\nToby - Human Resources")
# employee_file.write("\nKelly - Customer Service")
# employee_file.write("<p>This is HTML. We can use Python to write in HTML to create a site</p>")
# employee_file.close()
# import useful_tools
# print(useful_tools.roll_dice(10))
# import docx
# docx.
# from Student import Student
# student1 = Student("Jim", "Business", 3.1, False)
# print(student1.name)
# from Student import Student
# student1 = Student("Jim", "Business", "3.1", False)
# student2 = Student("Pam", "Art", "2.2", True)
# print(student1.name)
# print(student2.gpa)
# from Question import Question
# question_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "What color are bananas?\n(a) Black\n(b) Orange\n(c) Yellow\n\n",
#     "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
# ]
#
# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b")
# ]
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print("You got " + str(score) + "/" + str(len(questions)) + " correct.")
# run_test(questions)
# from Student import Student
# student1 = Student("Oscar", "Accounting", 3.1)
# student2 = Student('Phyllis', 'Business', 3.8)
#
# print(student1.on_honor_roll())
# print(student2.on_honor_roll())
# from Chef import Chef
# from ChineseChef import ChineseChef
#
# myChef = Chef()
# myChef.make_chicken()
#
# myChineseChef = ChineseChef()
# myChineseChef.make_orange_chicken()
# myChineseChef.make_special()

# print("    /|")
# print("   / |")
# print("  /  |")
# print(" /   |")
# print("/____|")

# character_name = "Tom"
# character_age = "50"
#
# print("There once was a man named " + character_name + ", ")
# print("he was " + character_age + " years old. ")
# character_name = "Mike"
# character_age = "44"
# print("He really liked the name " + character_name + ", ")
# print("but didn't like being " + character_age + ".")

# Variables/data can be string, numbers (integer, float), true or false (boolean)

# phrase = "Giraffe Academy"
# print("Giraffe\"\\\nAcademy")
# print(phrase + " is cool")
# print(phrase.lower())
# print(phrase.upper())
# print(phrase.isupper())
# print(phrase.upper().isupper())
# print(len(phrase))
# print(phrase[0])
# print(phrase.index("G"))
# print(phrase.index("Academy"))
# print(phrase.index("i"))
# print(phrase.replace("Giraffe", "Elephant"))

# print(10 % 3)

# from math import *
#
# my_num = -5
# print(str(abs(my_num)) + " is my favorite number")
# print(pow(3, 5))
# print(max(4, 5, 2, 1, 9))
# print(min(4, 2, 5, 7, 7, 2))
# print(round(3.2))
# print(floor(3.7))
# print(ceil(3.4))
# print(sqrt(36))

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age + "!")

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# print(result)

# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")
#
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#
# friends2 = friends.copy()
# print(friends2)

# coordinates = (4, 5)  # Tuples are like lists, but immutable. Tuples can be inside lists.
# # coordnates[1] = 10 ## This won't work since tuples are immutable
# print(coordinates[1])

# def sayhi(name, age):
#     print("Hello " + name + ", you are " + str(age) + ".")
#
# sayhi("Mike", 35)
# sayhi("Steve", 66)

# def cube(num):
#     return num*num*num
# result = cube(4)
# print(result)

# is_male = True
# is_tall = False
#
# if is_male and is_tall:
#     print("Person is a tall male.")
# elif is_male and not(is_tall):
#     print("Person is a short male.")
# elif not(is_male) and is_tall:
#     print("Person is tall, but not a male.")
# else:
#     print("Person is not male and not tall.")

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(3, 400, 5))

# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator.")

# monthConversions = {
#     "Jan" : "January",
#     "Feb" : "February",
#     "Mar" : "March",
#     "Apr" : "April",
#     "May" : "May",
#     "Jun" : "June",
#     "Jul" : "July",
#     "Aug" : "August",
#     "Sep" : "September",
#     "Oct" : "October",
#     "Nov" : "November",
#     "Dec" : "December"
# }
#
# print(monthConversions.get("Luv", "Key not found"))

# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# print("i is now " + str(i) + " Done with loop.")

# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess:")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("You are out of guesses. YOU LOSE.")
# else:
#     print("You got the secret word. YOU WIN.")

# friends = ["Jim", "Karen", "Kevin"]
# for index in range(5):
#     if index == 0:
#         print("First iteration")
#     else:
#         print("Not first")

# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
# print(raise_to_power(2, 3))

# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
#
# # print(number_grid[2][1])
#
# for row in number_grid:
#     for col in row:
#         print(col)

#  Giraffe Language
#  vowels -> g

#  dog -> dgg
#  cat -> cgt

# def translate(phrase):
#     final = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 final = final + "G"
#             else:
#                 final = final + "g"
#         else:
#             final = final + letter
#     return final
#
# print(translate(input("Enter a phrase: ")))

# try:
#     value = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid input")

# employee_file = open("employees.txt", "r")
#
# for employee in employee_file.readlines():
#     print(employee)
#
# employee_file.close()

employee_file = open("employees.txt", "a")

employee_file.write("\nToby - Human Resources")

employee_file.close()