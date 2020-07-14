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
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
from scipy.stats import ttest_ind
students = pd.read_csv('stud_math.csv')
def quantiles_info(columns):
    median = columns.median()
    IQR = columns.quantile(0.75) - columns.quantile(0.25)
    perc25 = columns.quantile(0.25)
    perc75 = columns.quantile(0.75)
    minimum = columns.min()
    maximum = columns.max()
    if minimum < (perc25 - 1.5*IQR) or maximum > (perc75 + 1.5*IQR):
        print ('Есть выбросы')
        print('Минимальное значение: {},'.format(minimum),'\nМаксимальное значение: {},'.format(maximum),
          "\nГраницы выбросов: [{f}, {l}],".format(f=perc25 - 1.5*IQR, l=perc75 + 1.5*IQR),'\n25-й перцентиль: {},'.format(perc25), '75-й перцентиль: {},'.format(perc75)
          , "IQR: {}, ".format(IQR),)
    else:
        print('Нет выбросов')
    

def missing_values_table(df):
    # Total missing values
    mis_val = df.isnull().sum()
        
    # Percentage of missing values
    mis_val_percent = 100 * df.isnull().sum() / len(df)
        
    # Make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        
    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Отсутствующие значения', 1 : '% от общего кол-ва '})
        
    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[mis_val_table_ren_columns.iloc[:,1] != 0].sort_values('% от общего кол-ва ', ascending=False).round(1)
        
    # Print some summary information
    print ("В датафрейме содержится " + str(df.shape[1]) + " колонок.\n" "В " + str(mis_val_table_ren_columns.shape[0]) +" колонках есть отсутствующие значения.")
        
    # Return the dataframe with missing information
    return mis_val_table_ren_columns 
    
def replace_nan_with_most_frequent(title):
    most_frequent = students[title].value_counts().index[0]
    students[title] = students[title].apply(lambda x: most_frequent if pd.isna(x) else x)
    
def replace_nan_with_value(title, value):
    students[title] = students[title].apply(lambda x: value if pd.isna(x) else x)

def replace_na_with_median():
    nan_columns = list(students.columns[students.isnull().sum() > 0])
    if nan_columns:
        for nan_column in nan_columns:
            students[nan_column+'_isNAN'] = pd.isna(students[nan_column]).astype('uint8')
        students.fillna(data.median(), inplace=True)
    
def get_stat_dif(column):
    cols = students.loc[:, column].value_counts().index
    combinations_all = list(combinations(cols, 2))
    for comb in combinations_all:
        if ttest_ind(students.loc[students.loc[:, column] == comb[0], 'score'], 
                        students.loc[students.loc[:, column] == comb[1], 'score']).pvalue \
            <= 0.05/len(combinations_all): 
            print('Найдены статистически значимые различия для колонки', column)
            break
            
def get_boxplot(column):
    fig, ax = plt.subplots(figsize = (14, 4))
    sns.boxplot(x=column, y='score', data=students, ax=ax)
    plt.xticks(rotation=45)
    ax.set_title('Boxplot for ' + column)
    plt.show()

# -


