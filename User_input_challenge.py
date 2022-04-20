'''
##############################
User Input Challenge
##############################

Create a program that asks the user to enter their name and their age. Print out a message 
addressed to them that tells them the year that they will turn 100 years old.

Add on to the previous program by asking the user for another number and printing out that 
many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n" is the same as pressing the ENTER button)
'''


current_year = 2022

name = input("What is your name?")

print(f"Hello {name}")

age = int(input("How old are you?"))

new_age = 100-age
print(f"You have {new_age} years until you turn 100")

old_age = new_age + current_year
print(f"You will turn 100 in the year {old_age}")