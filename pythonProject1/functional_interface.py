import algorithms_sugarbeet as sb
import matplotlib.pyplot as plt

def experiment(n, min_start_sugar, max_start_sugar, min_maturation, max_maturation, min_degradation, max_degradation):
    # numOfExperiments = 15
    # n = 50
    # min_start_sugar=0.4
    # max_start_sugar=0.9
    # min_maturation=1.03
    # max_maturation=1.07
    # min_degradation=0.95
    # max_degradation=0.91

    # numOfExperiments = int(input("Введите число экспериментов:\n "))
    # n = int(input("Введите размер матрицы:\n "))
    # min_start_sugar= float(input("введите нижнюю границу начальных значений матрицы:\n "))
    # max_start_sugar=float(input("введите верхнюю границу начальных значений матрицы:\n "))
    # min_maturation=float(input("введите нижнюю границу значений коэффициентов дозаривания:\n "))
    # max_maturation=float(input("введите верхнюю границу значений коэффициентов дозаривания:\n "))
    # min_degradation=float(input("введите нижнюю границу значений коэффициентов деградации:\n "))
    # max_degradation=float(input("введите верхнюю границу значений коэффициентов деградации:\n "))

    res1 = []
    res2 = []
    res3 = []
    res4 = []
    res5 = []
    res6 = []
    Days = [i + 1 for i in range(n)]

    # Вводим стартовые значения и интервалы - получаем матрицу P
    p = sb.rand_p_matrix(size=n, maturation=2,
                        min_start_sugar=min_start_sugar, max_start_sugar=max_start_sugar,
                        min_maturation=min_maturation, max_maturation=max_maturation,
                        min_degradation=min_degradation, max_degradation=max_degradation)

        # Вывод матрицы P
        # for i in range(len(p)):
        #     print(p[i])
            # Используем сгенерированную матрицу P и передаем ее в функции расчета
            # Венгерский минимальный
    r1, indices1, res1 = sb.hungarian_min(p)

            # Венгерский максимальный
    r2, indices2, res2 = sb.hungarian_max(p)

            # Жадный алгоритм
    r3, indices3, res3 = sb.greedy(p)

            # Бережливый алгоритм
    r4, indices4, res4 = sb.thrifty(p)

            # Бережливо-жадный алгоритм
    r5, indices5, res5 = sb.greedy_thrifty(p, n // 2)

            # Жадно-бережливый алгоритм
    r6, indices6, res6 = sb.thrifty_greedy(p, n // 2)

            #Days.append(i)

    print('\n')
    print("Целевая функция Венгерского минимума: " + str(r1))
    print("Целевая функция Венгерского максимума: " + str(r2))
    print("Целевая функция Жадного алгоритма: " + str(r3))
    print("Целевая функция Бережливого алгоритма: " + str(r4))
    print("Целевая функция Жадно-бережливого алгоритма: " + str(r5))
    print("Целевая функция Бережливо-жадного алгоритма: " + str(r6))

    plt.title("Сравнение алгоритмов")
    plt.xlabel("Число партий")
    plt.ylabel("S")
    plt.plot(Days, res1, linestyle = '-', color = 'black', label = "Венгерский мин")
    plt.plot(Days, res2, linestyle = '-', color = 'purple', label = "Венгерский макс")
    plt.plot(Days, res3, linestyle = '-', color = 'green', label = "Жадный")
    plt.plot(Days, res4, linestyle = '-', color = 'red', label = "Бережливый")
    plt.plot(Days, res5, linestyle = '-', color = 'blue', label = "Жадно-бережливый")
    plt.plot(Days, res6, linestyle = '-', color = 'brown', label = "Бережливо-жадный")
    plt.legend()
    plt.show()

    m2 = [0 for i in range(n)]
    m1 = [abs(res2[i] - res1[i]) / res1[i] for i in range(n)]
    m3 = [abs(res2[i] - res3[i]) / res3[i] for i in range(n)]
    m4 = [abs(res2[i] - res4[i]) / res4[i] for i in range(n)]
    m5 = [abs(res2[i] - res5[i]) / res5[i] for i in range(n)]
    m6 = [abs(res2[i] - res6[i]) / res6[i] for i in range(n)]

    plt.title("Сравнение ошибок")
    plt.xlabel("Число партий")
    plt.ylabel("Ошибка")
    plt.plot(Days, m1, linestyle = '-', color = 'black', label = "Венгерский мин")
    plt.plot(Days, m2, linestyle = '-', color = 'purple', label = "Венгерский макс")
    plt.plot(Days, m3, linestyle = '-', color = 'green', label = "Жадный")
    plt.plot(Days, m4, linestyle = '-', color = 'red', label = "Бережливый")
    plt.plot(Days, m5, linestyle = '-', color = 'blue', label = "Жадно-бережливый")
    plt.plot(Days, m6, linestyle = '-', color = 'brown', label = "Бережливо-жадный")
    plt.legend()
    plt.show()

def manual(n, matrix):
    r1, indices1, res1 = sb.hungarian_min(matrix)
    r2, indices2, res2 = sb.hungarian_max(matrix)
    r3, indices3, res3 = sb.greedy(matrix)
    r4, indices4, res4 = sb.thrifty(matrix)
    r5, indices5, res5 = sb.greedy_thrifty(matrix, n // 2)
    r6, indices6, res6 = sb.thrifty_greedy(matrix, n // 2)

    print("Целевая функция Венгерского минимума: " + str(r1))
    print("Целевая функция Венгерского максимума: " + str(r2))
    print("Целевая функция Жадного алгоритма: " + str(r3))
    print("Целевая функция Бережливого алгоритма: " + str(r4))
    print("Целевая функция Жадно-бережливого алгоритма: " + str(r5))
    print("Целевая функция Бережливо-жадного алгоритма: " + str(r6))

    # print("Венг. мин: ", r1, "\nВенг. макс: ", r2, "\nЖадный: ", r3)
    print("\nВенг. мин: ", indices1, "\nВенг. макс: ", indices2, "\nЖадный: ", indices3,
          "\nБережливый: ", indices4, "\nЖадно-бережливый: ", indices5, "\nБережливо-жадный: ", indices6)

experiment(50, 0.4, 0.5, 1.13, 1.17, 0.85, 0.81)
