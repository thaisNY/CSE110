import random
count = 1
play = 'yes'
while play == 'yes':
    #magic_num = int(input("What is the magic number?"))
    magic_num = random.randint(1, 100)
    print(magic_num)
    guess_num = ''
    while guess_num != magic_num:
        guess_num = int(input("What is your guess?"))
        if magic_num == guess_num:
            print("You guessed it!")
            print(f"You gueesed {count} time to get the right answers")
            count = 0
            play = input("Do you want to play again?").lower() 
            
        elif magic_num > guess_num:
            print("Higher")
        else:
            print("Lower")
        count += 1


