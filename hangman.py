import random
import string

words = ["hello","dinner","photosynthesis","quarterback"]


clues = []
used_letters = []

def play(lives,word):
   while True:
       if lives == 5:
           print("               |")
           print("               |")
           print("------------+")
           print(f"You have {lives} guesses remaining")

       if lives == 4:
           print(" +--------+")
           print("             |")
           print("             |")
           print(" +--------+")
           print(f"You have {lives} guesses remaining")

       if lives == 3:
           print(" +------------+")
           print(" |                 |")
           print("                   |")
           print("                   |")
           print("  -------------+")
           print(f"You have {lives} guesses remaining")

       if lives == 2:
            print("  +-------------+")
            print("  |                 |")
            print("  0                |")
            print("  |                 |")
            print("                    |")
            print("  --------------+")
            print(f"You have {lives} guesses remaining")

       if lives == 1:
           print("  +-------------+")
           print("  |                 |")
           print("  0                |")
           print(" <|>               |")
           print("                    |")
           print("  --------------+")
           print(f"You have {lives} guesses remaining")

       if lives == 0:
           print("   +-------------+")
           print("   |                 |")
           print("   0                |")
           print("  <|>               |")
           print("  ( )               |")
           print("  ---------------+")
           print(f"The word is : {word}")
           print("Game Over!!")
           break

       clue = [letter if letter in clues else "- " for letter in word]
       if word == ''.join(clue):
           print("You got it")
           break
       print(f"Used letters: {" ".join(used_letters)}")
       print(''.join(clue))
       guess = input("Guess: ")

       if guess == word:
           print("You got it")
           break

       while len(guess) > 1:
           print("You can only guess the whole word at once or\nguess one letter at a time")
           guess = input("Guess: ")

       if guess in word:
           clues.append(guess)
           if ''.join(clue) == word:
               print("You got it")
               break

       elif guess not in word:
           used_letters.append(guess)
           print("letter not in word")
           lives -= 1



lives = 5

print("- ".join(clues))
lives = 5
word = random.choice(words)
play(lives,word)