"""Game "Guess a number 2.0" 
(computer makes its own guess)"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Random number guesser

    Args:
        number (int, optional): The number. Defaults to 1.

    Returns:
        int: Amount of attempts
    """
    count=0
    
    while True:
        count+=1
        predict_number = np.random.randint(1,101) # guessed number
        if number==predict_number:
            break #cycle end after correct guess
    return(count)

def score_game(random_predict) -> int:
    """Average amount of attempts to guess a number in 1000 reps

    Args:
        random_predict ([type]): guess function

    Returns:
        int: average amount of attempts
    """
    count_ls = []
    np.random.seed(1) # fix the seed for reproducibility
    random_array = np.random.randint(1,101, size=(1000)) # Made a list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"The algorithm guesses a number in an average of {score} attempts")
    return(score)

if __name__=='__main__':
    # RUN
    score_game(random_predict)