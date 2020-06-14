# Number guessing game in python

import random
start= int(1)
finish = int(250)
random_num = random.randint(start,finish)

count = 0
while True:
    guess_num = int(input("Guess a number between "+str(start)+" and " +str(finish)+" : "))
    if guess_num < random_num:
        print("Try higher numbers")

    elif guess_num > random_num:

        print("try smaller numbers")
    else:
        if guess_num == random_num:
            print("You have successfully guessed the number "+str(random_num)+" in "+str(count)+" tries") 

    count +=1