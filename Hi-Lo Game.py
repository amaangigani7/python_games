import random

low = 1
high = 1000

print("Please enter a number between {} and {}. ".format(low, high))
input("Press ENTER to start.\n")

guesses = 1
while True:
    guess = low + (high-low)//2
    hi_low = input("My guess is {}. Should I guess higher or lower? "
                   "Enter 'h' or 'l' or c if my guess is correct"
                   .format(guess)).casefold()
    if hi_low == 'h':
        # Guess higher
        low = guess + 1

    elif hi_low == 'l':
        high = guess - 1

    elif hi_low == 'c':
        print("I guessed it right. I got it in {}".format(guesses))

    else:
        print("error")

    guesses = guesses + 1