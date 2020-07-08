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
def quantiles(columns):
    median = columns.median()
    IQR = columns.quantile(0.75) - columns.quantile(0.25)
    perc25 = columns.quantile(0.25)
    perc75 = columns.quantile(0.75)
    print('25-й перцентиль: {},'.format(perc25), '75-й перцентиль: {},'.format(perc75)
          , "IQR: {}, ".format(IQR),"Границы выбросов: [{f}, {l}].".format(f=perc25 - 1.5*IQR, l=perc75 + 1.5*IQR))
    
def replace_na_with_most_frequent(title):
    most_frequent = students[title].value_counts().index[0]
    students[title] = students[title].apply(lambda x: most_frequent if pd.isna(x) else x)
    
def replace_na_with_value(title, value):
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
            <= 0.05/len(combinations_all): # Учли поправку Бонферони
            print('Найдены статистически значимые различия для колонки', column)
            break
            
def get_boxplot(column):
    fig, ax = plt.subplots(figsize = (14, 4))
    sns.boxplot(x=column, y='score', data=students, ax=ax)
    plt.xticks(rotation=45)
    ax.set_title('Boxplot for ' + column)
    plt.show()
# -


