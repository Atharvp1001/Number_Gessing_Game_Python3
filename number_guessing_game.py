import random

random_number = random.randint(1,100)

while True:

    try:
        guess = int(input("Guess the number betwenn 1 and 100: "))
        
        if guess > random_number:
            print("Too High!!")

        elif guess < random_number:
            print("Too Low!!")

        elif guess == random_number:
            print("Congratulation! You guessed the number")
            break

    except ValueError: # we used this try except for not able to take input except integers
        print("Please enter a valid number")
        

