# 2) Задача: предложить улучшения кода для уже решённых задач
#  с помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
# Найти сумму чисел списка стоящих на нечетной позиции
# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

spisokStart=[1, 2, 3, 5, 1, 5, 3, 10]
spisokFinish1=[i for i in spisokStart if spisokStart.count(i)==1]
print(spisokFinish1)

spisokFinish2=[spisokStart[i] for i in range(0,len(spisokStart)+1) if i%2!=0]
print(sum(spisokFinish2))

n=int(input('Введите натуральное число n='))
def f(x):
    return 3*x+1
spisokFinish3={i: f(i) for i in range(1,n+1)}
print(spisokFinish3)