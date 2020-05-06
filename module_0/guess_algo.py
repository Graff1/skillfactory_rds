# -*- coding: utf-8 -*-
import numpy as np
import random
def score_game(game_core_v1):
    '''Let's run it 1000 times to deect the productivity of the algorithm'''
    count_ls = []
    np.random.seed(1)  #fix RANDOM SEED
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"The algorithm will quess the nimner after {score} attempts avg.")
    return(score)
def game_core_v2(number):
    '''Solution with binary search algorithm '''
    count = 0
    left = -1
    right = 100
    while right > left + 1:
        middle = (left + right) // 2
        count += 1
        if middle >= number:
            right = middle
        else:
            left = middle
    return count

