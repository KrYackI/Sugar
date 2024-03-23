import tools
import numpy
from scipy.optimize import linear_sum_assignment
from random import uniform
import time

# rand_p_matrix возвращает матрицу P для решения задачи оптимизации, используя заданные интервалы разброса начальных условий.
    #size - размер матрицы P, maturation - знаменатель дроби дозаривания (у нас = 2 -> дозаривание будет до size//2)
    #min_start_sugar, max_start_sugar - интервал разброса стартовых значений сахаристости (должны быть от 0 до 1!)
    #min_maturation, max_maturation - интервал разброса значений увеличения сахаристости на этапах дозаривания (должны быть больше 1!)
    #min_degradation, max_degradation - коэффициенты деградации будут от min_degradation до max_degradation (должны быть от 0 до 1!).
def rand_p_matrix(size: int, maturation: int, min_start_sugar: float, max_start_sugar: float,
                 min_maturation: float, max_maturation: float, min_degradation: float, max_degradation: float):

    sugar_cols = size // maturation
    degradation_cols = size - sugar_cols
    a_vector = tools.rand_vector(size, min_start_sugar, max_start_sugar) # стартовая сахаристость
    sugar_matrix = tools.rand_matrix(size, sugar_cols, min_maturation, max_maturation) # часть матрицы для дозаривания
    degradation_matrix = tools.rand_matrix(size, degradation_cols, min_degradation, max_degradation)# это деградирующая часть
    b_matrix = tools.combin_matrix(sugar_matrix, degradation_matrix)
    p_matrix = tools.create_p_matrix(a_vector, b_matrix)
    return p_matrix


def hungarian_min(p_matrix):
    #Возвращает результат и список-перестановку целевой функции, поиск худшего результата с помощью венгерского алгоритма.
    col_indices, row_indices = linear_sum_assignment(p_matrix) # Список "row_indices" содержит индексы строк,
                                                               # а список "col_indices" - индексы столбцов, которые образуют оптимальное назначение.
    result = 0
    summa = [] # S на каждом шаге
    
    for i in range(len(row_indices)):
        result += p_matrix[col_indices[i]][row_indices[i]]   # итоговая сумма
        summa.append(result)
    for i in range(len(row_indices)):
        col_indices[row_indices[i]] = i
    return result, row_indices, summa


def hungarian_max(p_matrix):
    #Возвращает результат и список-перестановку целевой функции, поиск лучшего результата с помощью венгерского алгоритма.
    reverse_p_matrix = numpy.copy(p_matrix) #обратная матрица
    for i in range(len(p_matrix)):
        max_elem = numpy.max(p_matrix[i])
        for j in range(len(p_matrix)):
            reverse_p_matrix[i][j] = -1 * p_matrix[i][j] + max_elem # сводим максимизацию к минимизации
                                                                    #(в каждой строке берем максимальный элемент и вычитаем из него все остальные элементы строки)

    col_indices, row_indices = linear_sum_assignment(reverse_p_matrix)
    result = 0
    summa = []

    for i in range(len(row_indices)):
        result += p_matrix[col_indices[i]][row_indices[i]]
        summa.append(result)

    for i in range(len(row_indices)):
        col_indices[row_indices[i]] = i
    return result, row_indices, summa


def greedy(p_matrix: list):
    #Возвращает результат и список-перестановку целевой функции, поиск результата с помощью жадного алгоритма.
    result = 0
    indices = []
    took = []
    summa = []

    for j in range(len(p_matrix)): # идем по столбцам
        col_max = 0
        col_max_index: int
        for i in range(len(p_matrix)): # по строкам данного столбца
            is_took = False

            for k in range(len(took)):
                if took[k] == i:
                    is_took = True
                    break

            if is_took: # если такой элемент уже брали, то переходим к следующему
                continue

            if p_matrix[i][j] > col_max:
                col_max = p_matrix[i][j]
                col_max_index = i
        result += col_max
        summa.append(result)
        indices.append(col_max_index)
        took.append(col_max_index)
    return result, indices, summa


def thrifty(p_matrix: list):
    #Возвращает результат и список-перестановку целевой функции, поиск результата с помощью бережливого алгоритма.
    result = 0
    indices = []
    took = []
    summa = []
    
    for j in range(len(p_matrix)):
        col_min = 1000
        col_min_index: int
        for i in range(len(p_matrix)):
            is_took = False

            for k in range(len(took)):
                if took[k] == i:
                    is_took = True
                    break

            if is_took:
                continue

            if p_matrix[i][j] < col_min:
                col_min = p_matrix[i][j]
                col_min_index = i
        result += col_min
        summa.append(result)
        indices.append(col_min_index)
        took.append(col_min_index)
    return result, indices, summa


def thrifty_greedy(p_matrix: list, saving_steps: int):
    #Возвращает результат и список-перестановку целевой функции, поиск результата с помощью бережливо-жадного алгоритма.
    #saving_steps - количество шагов в режиме сбережения, далее будет жадный режим.
    result = 0
    indices = []
    took = []
    summa = []
    saving_steps_completed = 0

    for j in range(len(p_matrix)):

        col_min = 10
        col_min_index: int

        col_max = 0
        col_max_index: int
        saving = False

        if saving_steps_completed < saving_steps:
            saving = True

        for i in range(len(p_matrix)):
            is_took = False

            for k in range(len(took)):
                if took[k] == i:
                    is_took = True
                    break

            if is_took:
                continue

            if saving and p_matrix[i][j] < col_min:
                col_min = p_matrix[i][j]
                col_min_index = i

            if not saving and p_matrix[i][j] > col_max:
                col_max = p_matrix[i][j]
                col_max_index = i

        if saving:
            result += col_min
            summa.append(result)
            indices.append(col_min_index)
            took.append(col_min_index)

        else:
            result += col_max
            summa.append(result)
            indices.append(col_max_index)
            took.append(col_max_index)

        saving_steps_completed += 1

    return result, indices, summa



def greedy_thrifty(p_matrix: list, greedy_steps: int):
    #Возвращает результат и список-перестановку целевой функции, поиск результата с помощью жадно-бережливого алгоритма.\n
    #greedy_steps - количество шагов в режиме жадности, далее будет бережливый режим.
    result = 0
    indices = []
    took = []
    summa = []
    greedy_steps_completed = 0

    for j in range(len(p_matrix)):

        col_min = 1000
        col_min_index: int

        col_max = 0
        col_max_index: int
        greedy = False
        
        if greedy_steps_completed < greedy_steps:
            greedy = True

        for i in range(len(p_matrix)):
            is_took = False

            for k in range(len(took)):
                if took[k] == i:
                    is_took = True
                    break

            if is_took:
                continue

            if not greedy and p_matrix[i][j] < col_min:
                col_min = p_matrix[i][j]
                col_min_index = i

            if greedy and p_matrix[i][j] > col_max:
                col_max = p_matrix[i][j]
                col_max_index = i

        if greedy:
            result += col_max
            summa.append(result)
            indices.append(col_max_index)
            took.append(col_max_index)

        else:
            result += col_min
            summa.append(result)
            indices.append(col_min_index)
            took.append(col_min_index)

        greedy_steps_completed += 1

    return result, indices, summa



