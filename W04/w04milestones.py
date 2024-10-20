"""
Showing creative:
-Limited number of guesses to 5 or less
-Random secret word
"""
import random

word_list = ['temple', 'moroni', 'alma', 'god', 'jessus', 'mormon']
secret = random.choice(word_list)
guess = ''
print("Welcome to the word guessing game!")
count = 0
while guess != secret:
    print("Your hint is: ", end = ' ')
    hint = ""
    for i in range(len(secret)):
        hint += "-"
    print(hint)
    guess = input("What is your guess?").lower()
    if len(guess) != len(secret):
        print("Your guess has a different number of letters than the number of letters in the secret.Try again!")
       
        continue
    hint = ""
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            hint += guess[i].upper()
        elif guess[i] in secret: 
             hint += guess[i].lower()
        else:
            hint += "-"
    count += 1
    print("Your hint is:", hint)
    if count >= 5:
        print("You lose!")

if guess == secret:
    print("Congratulations! You guessed it!")
    print(f"It took you {count} guesses.")