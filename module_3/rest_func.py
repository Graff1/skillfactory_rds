# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# Создаем функцию для перевода ценового диапазона в числовое значение
def price_range(row):
    if row['Price Range'] == '$':
        return 1
    elif row['Price Range'] == '$$ - $$$':
        return 2
    elif row['Price Range'] == '$$$$':
        return 3
    else:
        return 0

# Функция подсчета количества кухонь в каждом ресторане


def filter_cuisine_style(line):
    if pd.isnull(line):
        return ['one']
    else:
        line = line.replace('[','')
        line = line.replace(']', '')
        line = line.strip()
        line = [style.strip() for style in line.split(',')]
        line = [style for style in line if len(style) > 0]
        return line
    
def calculate_cuisines(row):
    return len(row['Cuisine Style'].split(','))

#Обработка отзывов
def reviews_to_list(line):
    if pd.isnull(line):
        return ['one']
    else:
        line = line.replace(']]', '')
        line = line.replace("'", '')
        line = line.split('], [')[1]
        line = line.split(', ')
        return line
