
def preference():
    answer = input("hi, do you wanna play a game?: ")

    if answer == "yes":
        print("schweet!")
        from time import sleep
        sleep(1.4)  # Time in seconds
        print("i knew you would make the right choice")
        from time import sleep
        sleep(1.2)  # Time in seconds
    else:
        print("welp you dont have a choice")


preference()

from time import sleep

sleep(1.5)  # Time in seconds

print("hmmmm lets see if you can guess what number im thinking of!")

from time import sleep

sleep(3)  # Time in seconds

print("theres an infinte amount of choices, eh?")

from time import sleep

sleep(3)  # Time in seconds

print("ill be nice and let you pick a range")

from time import sleep

sleep(3)  # Time in seconds

lowerbound = int(input("whats the smallest number?:"))
upperbound = int(input("now the largest number:"))

import random
randomNum = random.randint(lowerbound, upperbound)
print("hmmmm very intresting choices. now i will pick a number in between")


from time import sleep

sleep(1)  # Time in seconds

#start guessing
guess = input("any guesses what number it could be: ")

