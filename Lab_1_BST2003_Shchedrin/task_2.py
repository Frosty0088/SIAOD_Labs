from random import randint



### Задание №2
# Написать генератор случайных матриц(многомерных), который принимает
# опциональные параметры m, n, min_limit, max_limit, где m и n указывают размер
# матрицы, а min_lim и max_lim - минимальное и максимальное значение для
# генерируемого числа . По умолчанию при отсутствии параметров принимать следующие
# значения:
# m = 50
# n = 50
# min_limit = -250
# max_limit = 1000 + (номер своего варианта)

# In[ ]:
answer = str(input('Введите да или нажмите "Enter": '))

def M_create():
        if answer == 'Да' or answer == 'да':
            m = int(input('Введите количество строк: '))
            n = int(input("Введите количество столбцов: "))
            min_limit = int(input("Укажите начальный диапозон чисел для генерации: "))
            max_limit = int(input("Укажите конечный диапозон чисел для генерации: "))
            matrix = [[randint(min_limit, max_limit + 1) for j in range(m)] for i in range(n)]
            return matrix

        elif answer == "":
            m = 50
            n = 50
            min_limit = -250
            max_limit = 1000 + 16
            matrix = [[randint(min_limit, max_limit + 1) for j in range(m)] for i in range(n)]
            return matrix
        else:
            matrix = ["Ответьте на вопрос Да или нажмите 'Enter'"]
            return matrix

def M_output():
    matrix = M_create()
    print('Матрица: ')
    for i in range(len(matrix)):
        print(matrix[i])

##M_output()


