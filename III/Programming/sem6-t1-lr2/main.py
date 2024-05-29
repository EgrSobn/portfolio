# Программирование (Python)
# 6 семестр, тема 1

# Лабораторная работа 2
"""
Используя обучающий набор данных о пассажирах Титаника, находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), найдите ответы на следующие вопросы: 

1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.

2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.

3. Посчитайте долю (процент) погибших на параходе (число и процент)?

4. Какие доли составляли пассажиры первого, второго, третьего класса?

5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).

6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
1) возрастом и параметром Survived;
2) полом человека и параметром Survived;
3) классом, в котором пассажир ехал, и параметром Survived.

7. Посчитайте средний возраст пассажиров и медиану.
8. Посчитайте среднюю цену за билет и медиану.

9. Какое самое популярное мужское имя на корабле?
10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?


Для вычисления 3, 4, 5, 6, 7, 8 используйте тип данных float с точностью два знака в дробной части. 
"""

import pandas as pd
import numpy as np

data = pd.read_csv('train.csv', index_col="PassengerId")


# TODO #1
def get_sex_distrib(data):
    """
    1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
    """
    n_male, n_female = 0, 0
    res = data['Sex'].value_counts()
    n_male, n_female = res['male'], res['female']
    n_male, n_female = int(n_male), int(n_female)
    return n_male, n_female


print(f'Количество мужчин и женщин: {get_sex_distrib(data)} \n')


# TODO #2
def get_port_distrib(data):
    """  
    2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
    """

    port_S, port_C, port_Q = 0, 0, 0
    res = data['Embarked'].value_counts()
    port_S, port_C, port_Q = res['S'], res['C'], res['Q']
    return port_S, port_C, port_Q


print(
    f'Пассажиров загрузилось на борт в различных портах {get_port_distrib(data)} \n'
)


# TODO #3
def get_surv_percent(data):
    """
    3. Посчитайте долю погибших на параходе (число и процент)?
    """

    n_died, n_alive, perc_died = 0, 0, 0
    res = data['Survived'].value_counts()
    print(f'test for value_counts {res}')
    n_died, n_alive = res[int(0)], res[int(1)]
    perc_died = round(n_died * 100 / (n_died + n_alive), 2)
    perc_died = str(perc_died) + "%"
    return n_died, perc_died


print(
    f'Доля погибших на параходе (число и процент) {get_surv_percent(data)} \n')


# TODO #4
def get_class_distrib(data):
    """
    4. Какие доли составляли пассажиры первого, второго, третьего класса?    
    """
    n_pas_first_cl, n_pas_second_cl, n_pas_third_cl = 0, 0, 0
    list = []
  
    res = data['Pclass'].value_counts()
    n_pas_first_cl, n_pas_second_cl, n_pas_third_cl = res[int(1)], res[int(
        2)], res[int(3)]
    n_all_pass = n_pas_first_cl + n_pas_second_cl + n_pas_third_cl

    append = lambda x: list.append(x)
    append(n_pas_first_cl)
    append(n_pas_second_cl)
    append(n_pas_third_cl)
    list = list / n_all_pass
    my_formatted_list = [ float('%.2f' % elem) for elem in list ]
    assert sum(my_formatted_list) == 1.0
    return my_formatted_list


print(
    f'Доли составляли пассажиры первого, второго, третьего класса {get_class_distrib(data)} \n'
)


# TODO #5
def find_corr_sibsp_parch(data):
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """

    corr_val = -1
    data_frame = pd.DataFrame(data)
    corr_val = round(data_frame['SibSp'].corr(data_frame['Parch']), 2)
    return corr_val


print(f'Коэффициент корреляции Пирсона (количество супругов и детей): {find_corr_sibsp_parch(data)} \n')


# TODO #6-1
def find_corr_age_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - возрастом и параметром Survived;

    """

    corr_val = -1
    data_frame = pd.DataFrame(data)
    corr_val = round(data_frame['Age'].corr(data_frame['Survived']), 2)
    return corr_val

print(f'Коэффициент корреляции Пирсона (выживаемость от возраста): {find_corr_age_survival(data)} \n')

# TODO #6-2
def find_corr_sex_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - полом человека и параметром Survived;
    """
    corr_val = -1
    data_frame = pd.DataFrame(data)
    data_frame = data_frame.replace({'Sex' : { 'male' : int(0), 'female' : int(1)}})
    corr_val = round(data_frame['Sex'].corr(data_frame['Survived']), 2)
    return corr_val

print(f'Коэффициент корреляции Пирсона (выживаемость от пола): {find_corr_sex_survival(data)} \n')

# TODO #6-3
def find_corr_class_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

    - классом, в котором пассажир ехал, и параметром Survived.
    """

    corr_val = -1
    data_frame = pd.DataFrame(data)
    corr_val = round(data_frame['Pclass'].corr(data_frame['Survived']), 2)
    return corr_val

print(f'Коэффициент корреляции Пирсона (выживаемость от класса): {find_corr_class_survival(data)} \n')

# TODO #7
def find_pass_mean_median(data):
    """
    7. Посчитайте средний возраст пассажиров и медиану.
    """
    data_frame = pd.DataFrame(data)
    mean_age, median = None, None
    median = data_frame['Age'].median()
    mean_age = round(data_frame['Age'].mean(), 2)
    return mean_age, median

print(f'Средний возраст и медиана: {find_pass_mean_median(data)}')

# TODO #8
def find_ticket_mean_median(data):
    """
    8. Посчитайте среднюю цену за билет и медиану.
    """
    data_frame = pd.DataFrame(data)
    mean_price, median = None, None
    mean_price, median = round(data_frame['Fare'].mean(), 2), round(data_frame['Fare'].median(), 2)
    return mean_price, median

print(f'Средняя цена за билет и медиана: {find_ticket_mean_median(data)}')

# TODO #9
def find_popular_name(data):
    """
    9. Какое самое популярное мужское имя на корабле?
    """
    name = None
    data_frame = pd.DataFrame(data)
    sex = {'male':1, 'female':0}
    data_frame['Sex'] = data_frame['Sex'].map(sex)
    #if data_frame['Sex'] == 
    return name

print(find_popular_name(data))

# TODO #10
def find_popular_adult_names(data):
  pass

    # popular_male_name, popular_female_name = "", ""
    # return popular_male_name, popular_female_name
# ------------------------------

# Реализуем вычисление количества пассажиров на параходе и опишем предварительные действия с данными (считывание)

# После загрузки данных с помощью метода read_csv и индексации его по первому столбцу данных (PassangerId) становится доступно выборка данных по индексу.
# С помощью запроса ниже мы можем получить имя сотого пассажира
# print(type(data.iloc[100]))
# print(data.iloc[100]['Name'])

# print((data['Name'], data['Sex']))

# print(find_corr_sex_survival(data))


def test_get_number_of_pass():
    assert get_sex_distrib(data) == (577, 314), f'Неверно'


#def test_

test_get_number_of_pass()
# # аналогично протестировать остальные функции
