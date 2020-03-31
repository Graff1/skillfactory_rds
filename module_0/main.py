import numpy as np
import random
def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
def game_core_v2(number):
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
score_game(game_core_v2)
