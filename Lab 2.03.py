'''
##########################################
Lab 2.03 - Game Show
##########################################
In your Notebook
Follow the flow of execution in the following programs and predict what will happen for each
one
---------------------------------------
Example 1
---------------------------------------
a = input("What... is your quest")
b = "to seek the holy grail"
if a != b:
    print("Go On. Off you go")
else:
    b = input("What...is the air-speed velocity of an unladen swallow?")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHHH [Bridgekeeper was thrown over bridge]")
    else:
        print("[you were thrown over bridge]")

Prediction: If I do not respond with searching holy grail the code will end. If I respond right I get asked a question and someone will then be thrown off a bridge
Actual: The problem is it will work but you can't space when responding in the Terminal.

---------------------------------------
Example 2
---------------------------------------
user_input = input("What is your favorite color")
if user_input == 'blue':
    print("Blueskadoo")
elif user_input == "red":
    print("Roses are red!")
elif user_input == "yellow":
    print("Mellow Yellow")
elif user_input == "green":
    print("Green Machine")
elif user_input == "orange":
    print("Orange you glad I didn't say banana.")
elif user_input == "black":
    print("I see a red door and I want it painted black")
elif user_input == "purple":
    print("And we'll never be royalllssss")
elif user_input == "pink":
    print("Pinky- and the Brain")
else:
    print("I don't recognize that color. Is it even...??")

Prediction: Putting a color name will spit back a result
Actual: Works however my only problem is not being able to hit space so the response doesnt seem clumped with the question.

---------------------------------------
In your Notebook
---------------------------------------
Translate this Snap! program into a Python program
***Refer to the image provided on Moodle located below the Lab 2.03 link***
Write program below:

x = int(input("What is X?"))

y = int(input("What is Y?"))

z = int(input("What is Z?"))

if x + y > z and x + z > y and y + z > x:
    print(f"Perimeter of the triangle is {x + y + z}" ) 
    if x * x + y * y == z * z: 
        print("This is a right triangle!")
    else:
        if x == y and y == z:
            print("This is an equilateral Triangle!")
        else:
            print("This is a scalene triangle!")

else: 
    print("Sorry those inputs don't make a triangle!")

---------------------------------------
Create a game show program
---------------------------------------
Declare 10 prizes (prize1, prize2, prize 3 at the top of your file)
User picks a number
The prize corresponding with that door is printed for the user.
Write code below the multiline comment
'''
prizes = ['prize1, prize2, prize3, prize4, prize5, prize6, prize7, prize8, prize9, prize10']

x = int(input("Choose a prize!"))

if x == 1:
    print("You recieve prize1!")
elif x == 2:
    print("You receive prize 2!")
elif x == 3:
    print("You recieve prize 3!")
elif x == 4:
    print("You recieve prize 4!")
elif x == 5:
    print("You recieve prize 4!")
elif x == 5:
    print("You recieve prize 5!")
elif x == 6:
    print("You recieve prize 6!")
elif x == 7:
    print("You recieve prize 7!")
elif x == 8:
    print("You recieve prize 8!")
elif x == 9:
    print("You recieve prize 9!")
elif x == 10:
    print("You recieve prize 10!")
else:  
    print("That number does not give a prize")









