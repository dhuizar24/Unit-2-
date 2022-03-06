'''
###########################
Lab 2.04
###########################
1. In your notebook
For each example below, predict what will be printed. Run the program and write down the output in your notebook.

Example 1
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[0])
    print(a[3])

    prediction: The letters a and d will be printed                                    
    actual: a and d were printed

Example 2
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 3])

    prediction: can't tell
    actual: c

Example 3
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 6])

    prediction: e will print
    actual: e 

Example 4
    a = ['a', 'b', 'c', 'd', 'e']
    a[3] = 'haha'
    print(a)

    prediction: d will be replaced with haha 
    actual: a b c haha e

2. Create this game again using lists and indexes
--------------------------------------------------
Declare 10 prizes (prize0, prize1, prize2 at the top of your file), but store them all in a list.

User picks a number.

Print prize associated with the door user picked.
code below: 
prizes = ['Jet', 'Xbox', 'Playstation', 'Boat', 'Car', 'Vacation', 'Dog', 'Nintendo', 'Space Ship', 'Ten million dollars']

x = int(input("Choose a prize from a door one through ten!"))


print(f'You win a {prizes[x]}!')



3. Create a quiz
--------------------------------------------------
Create a food quiz using lists and indexes.

List of 6 different foods.

Ask the user 8 vague questions to find out what their favorite food is using the list.

Update the score and print their top 2 favorite foods.

Hint: Use a search engine to find the largest number in a python list.

----------------------
​Starter code here​:
----------------------
food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1

##############################
Together in class:
##############################
Research nested lists and work through the following Examples:

Bonus Example 1
a = ['a', 'b', 'c', ['d', 'e']]
print(len(a))
Bonus Example 2
a = ['a', 'b', 'c', ['d', 'e']]
b = a[3]
print(b)
Bonus - In your Notebook
How would you access d from the list a?
'''
questions = {"Do you like food with holes? " : ["donuts", "bagels"],
                "Do you like food from animals? " : ["bacon", "eggs"],
                "Do you like warm food? " : ["pancakes", "bacon", "waffles", "eggs"],
                "Do you like baked food?" : ["donuts", "bagels"],
                "Can your food also be a desert?" : ["donuts"],
                "Does your food also work during dinner?" : ["bacon", "eggs"],
                "Does your food taste sweet?" : ["donuts", "pancakes", "waffles"],
                "Does your food have a lot of oil and grease?" : ["bacon"],
                "Do you like brown colored food?" : ["bacon"],
                "Can your food come from a bakery?" : ["donuts", "bagels"],}


scores = {"donuts" : 0,
          "pancakes" : 0,
          "bacon" : 0,
          "waffles" : 0,
          "eggs" : 0,
          "bagels" : 0}


def start_quiz():
    print('Please answer each questions with "y" for "yes" and "n" for "no."')
    for question in questions:
        ask_question(question, questions[question])
    print(scores)


def ask_question(question, foods):
    user_input = input(question)
    while user_input.upper() != 'Y' and user_input.upper() != 'N':
        print("Please enter y or n")
        user_input = input("y or y?: ")
    if user_input.lower() == 'y':
        for food in foods:
            scores[food] += 1

def start_quiz():
    print('Please answer each questions with "y" for "yes" and "n" for "no."')
    for question in questions:
        ask_question(question, questions[question])
    favorites = sorted(scores, key=scores.get, reverse=True)[:2]
    print("\n-= QUIZ RESULTS =-")
    for score in scores:
        print(score + " : " + str(scores[score]))
    print("\nYour favorite foods are: ")
    for food in favorites:
        print(food)

start_quiz()



