from art import logo
import random


endOrContin = False

while not endOrContin:

  print(logo)
  print("Welcome to the number guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  print(f"psst, the correct answer is {random.randint(1,100)}")

  level = input("Choose a difficulty. Type 'easy' or 'hard'")

  flag = 0
  
  if level == 'easy':
    flag = 10
    value = random.randint(1,100)
    
    print(f"You have {flag} attempts remaining to guess the number")

    for _ in range(flag):
      guess = int(input("make a guess:"))

      if guess > value:
        flag -= 1
        print("Too High")
        print("Guess again")
        print(f"You have {flag} attempts remaining to guess the number")
      if guess < value:
        flag -= 1
        print("Too Low")
        print("Guess again")
        print(f"You have {flag} attempts remaining to guess the number")
      if guess == value:
        print(f"You got it! The answer was {value}")
        endOrContin = input("Would you like to continue? 'Yes' or 'No' ?")
        if endOrContin.lower() == 'yes':
          endOrContin = False
        if endOrContin.lower() == 'no':
          endOrContin = True
      if flag == 0:
        print("you lose")
        endOrContin = input("Would you like to continue? 'Yes' or 'No' ?")
        if endOrContin.lower() == 'yes':
          endOrContin = False
        if endOrContin.lower() == 'no':
          endOrContin = True
      
  if level.lower() == 'hard':
    flag = 5
    value = random.randint(1,100)
    
    print(f"You have {flag} attempts remaining to guess the number")

    for _ in range(flag):
      guess = int(input("make a guess:"))

      if guess > value:
        flag -= 1
        print("Too High")
        print("Guess again")
        print(f"You have {flag} attempts remaining to guess the number")
      if guess < value:
        flag -= 1
        print("Too Low")
        print("Guess again")
        print(f"You have {flag} attempts remaining to guess the number")
      if guess == value:
        print(f"You got it! The answer was {value}")
        endOrContin = input("Would you like to continue? 'Yes' or 'No' ?")
        if endOrContin.lower() == 'yes':
          endOrContin = False
        if endOrContin.lower() == 'no':
          endOrContin = True
      if flag == 0:
        print("you lose")
        endOrContin = input("Would you like to continue? 'Yes' or 'No' ?")
        if endOrContin.lower() == 'yes':
          endOrContin = False
        if endOrContin.lower() == 'no':
          endOrContin = True
