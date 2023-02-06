# Написать метод, который определяет, какие элементы присутствуют в двух экземплярах в каждом из массивов
# (= в двух и более, причем в каждом). На вход подаются два массива. На выходе массив с необходимыми совпадениями.
# Пример:
# [7, 17, 1, 9, 1, 17, 56, 56, 23], [56, 17, 17, 1, 23, 34, 23, 1, 8, 1]
# На выходе [1, 17]

# Решил примерно за 25 минут

def f(Array1, Array2):
    Array = []
    for i in Array1:
        if i in Array1 and i in Array2 and not (i in Array) and Array1.count(i) > 1 and Array2.count(i) > 1:
            Array += [i]
    for i in Array2:
        if i in Array1 and i in Array2 and not (i in Array) and Array1.count(i) > 1 and Array2.count(i) > 1:
            Array += [i]
    return Array


print(f([7, 17, 1, 9, 1, 17, 56, 56, 23], [56, 17, 17, 1, 23, 34, 23, 1, 8, 1]))
