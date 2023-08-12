from art import logo 


import random 
import math 
import replit


def guess_the_number():
  print(logo)
  answer = random.randint(1,100)
  
  print(f"\nWelcome to Guess The Number !")
  difficulty = input("Do you want an easy challenge or a hard challenge? (easy/hard) ")
  
  difficulty = difficulty.lower()
  
  if difficulty == 'easy':
    counter = 10
  
  elif difficulty == 'hard':
    counter = 5
  print(f"You are going to be guessing a number between 1 and 100, you have {counter} tries, good luck !")
  
  while counter > 0:
    guess = int(input("Guess a number: "))
    if guess > 100 or guess <1:
      print("You guessed a number outside the range, try again between 1 and 100.")
  
    elif guess > answer:
      counter -=1
      print(f"Too high. You have {counter} tries left. ")
  
    elif guess < answer:
      counter-=1
      print(f"Too low. You have {counter} tries left")
  
    elif guess == answer:
      print(f"You got it ! The answer is {answer}")
      counter = -1
  
    else:
      print(f"You ran out of tries. You lost.")
  
  play_again = input('Do you want to play again? (yes/no): ')

  if play_again.lower()=='yes':
    replit.clear()
    guess_the_number()
  elif play_again.lower()=='no':
    print(f"\nIt was fun while it lasted")
    return 

guess_the_number()
  
