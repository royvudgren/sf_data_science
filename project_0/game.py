"""Игра "Угадай число" """

import numpy as np

number=np.random.randint(1,101) #pick a number

#количество попыток
count = 0

while True:
    count+=1
    predict_number = int(input("Guess a number from 1 to 100: "))
    
    if predict_number > number:
        print("The number must be less! Guess again.")
    elif predict_number < number:
        print("The number must be greater! Guess again.")
    else:
        print(f"You've guessed by {count} attempts! The number is {number}")
        break #end of a game when the number is guessed