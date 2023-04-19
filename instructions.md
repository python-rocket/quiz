# Instructions  

  
## Goal of this Project
Now you will create your first Python program. You will create an interactive Quiz Game. This   Quiz Game uses everything you learned in the Basiscs course so far! You will see all the knowledge you learned in action of a real program. Also you will be able to adjust the game yourself. Having your own game in your portfolio will proof that you know the most important basics of Python.

## Checkout the Game
 Click on the Green "RUN" Button. This will run the whole Code and start the Quiz Game.
 Follow the instructions and play this game. Take a look at everything you see. Because next you will create it yourself.


## Structure of the Program

Basically the program will ask the user questions to different topics. 
We will check if the provided answer was correct. The score of the user will be saved in a ranking file.

In this Quiz game we want to include following logics in this order:

1) Input from the User (interacting with the program)
2) User should choose a topic (different topics will have different questions)
3) User should answer a question of this topic
4) User should see if his answer was correct or not
5) The game should have many rounds
6) For every right answer user gets a point
7) Save the score of the user in a file.
8) Get the salutation of a user based on his name
9) Outsource all Print Statements into one function
10) Add a "Play Again" functionality at the end of the game


## LETS GET STARTED

When writing a program you want to cut the logic into many small pieces. For every step above we will create our own functions. Then we will add those functions into our main program.

## 1. Input from the User
a) Write a Function which asks the User for his name. Then say hello to the user using his name. Save your own function in a seperate file.

*HINTS:*
- Use the function input()
- Use a variable to store the name
- Use a print function to say hello

*Learn Resources:*
- Check out following chapters of the Python Basics course: print, variables, functions



## 2. User should choose a topic
*TASKS:*
- Choose 3 different topics for questions (e.g Sport or Animals)
- The user should be asked to choose one of those 3 topics.
- If the user input is not one of those 3 topics, he should be asked again until he gives one of those 3 topics as an input.

*HINTS:*
- Save the 3 topics in a list
- Use the function input() to ask the user for a topic
- Use a variable to store the topic the user chose
- To check if the user choose one of the 3 possible topic options use a "if statement"
- To ask the question again until the user chooses one of the 3 topics use a "while loop"


*Learn Resources:*
- Check out following chapters of the Python Basics course: print, variables, functions, while loop, if else condition


## 3. User should answer a question of this topic
*TASKS:*
- The user has to choose one of the 3 topics.
- For every topic there should be at least 2 questions with answer.
- The answer of the question should always be a number. Make sure to add questions where the answer can be a number. (e.g: how many eyes has a person?)
- The user should get a random question of the topic he chose.
- At this point the user doesnt has to give an answer yet.


*HINTS:*
- Write a Function which has the variable "topic" as an input parameter
- Inside this function create a Dictionary with a key for each topic
- The value for each key should be a list
- In this list you will have Sets with 2 values. The first value is the question. The second value is the right answer. This set can look like this: ("How many eyes does a horse have?", 2)
- To get a random element of a list (to get a random question of one topic) you can use the "choice" function:
```python
from random import choice
colours = ["blue", "yellow", "green"]
print(choice(colours))
```

*Learn Resources:*
- Check out following chapters of the Python Basics course: variables, functions, lists, sets, dictionaries


## 4. User should see if his answer was correct or not
*TASKS:*
- Now the user should give an answer to the question.
- Make sure the user only gives a number as an answer. If he doesnt, let him know he should use a number and ask him again.
- After the user has answered with a number let him know if the answer was correct.


*HINTS:*
- Use try and except block to give an exception if the user is not giving a number as an answer.
- Use a while loop to aks the question again until he uses a number.
- Use an If Else Condition to check if the input of the user is the same as the answer. If yes, print him that he was correct 

*Learn Resources:*
- Check out following chapters of the Python Basics course: print, variables, functions, while loop, if else condition, sets

