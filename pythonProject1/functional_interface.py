import algorithms_sugarbeet as sb
import matplotlib.pyplot as plt

def experiment(n, mu, min_start_sugar, max_start_sugar, min_maturation, max_maturation, min_degradation, max_degradation):
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
    r5, indices5, res5 = sb.greedy_thrifty(p, mu)

            # Жадно-бережливый алгоритм
    r6, indices6, res6 = sb.thrifty_greedy(p, mu)

    r7, indices7, res7 = sb.TkG(p, mu, 2)
    k = 1
    for i in range(3, mu):
        r, ind, res = sb.TkG(p, mu, i)
        if (r7 < r):
            r7 = r
            indices7 = ind
            res7 = res
            k = i

    r8, indices8, res8 = sb.CTG(p, mu, 2)
    k2 = 1
    for i in range(3, n):
        r, ind, res = sb.CTG(p, mu, i)
        if (r8 < r):
            r8 = r
            indices8 = ind
            res8 = res
            k2 = i

    r9, indices9, res9 = sb.Gk(p, mu, 2)
    k3 = 1
    for i in range(3, n):
        r, ind, res = sb.Gk(p, mu, i)
        if (r9 < r):
            r9 = r
            indices9 = ind
            res9 = res
            k3 = i

            #Days.append(i)

    S = []

    # print('\n')
    S.append("Целевая функция Венгерского минимума: " + str(format(r1, '.4f')))
    S.append("Целевая функция Венгерского максимума: " + str(format(r2, '.4f')))
    S.append("Целевая функция Жадного алгоритма: " + str(format(r3, '.4f')))
    S.append("Целевая функция Бережливого алгоритма: " + str(format(r4, '.4f')))
    S.append("Целевая функция Жадно-бережливого алгоритма: " + str(format(r5, '.4f')))
    S.append("Целевая функция Бережливо-жадного алгоритма: " + str(format(r6, '.4f')))
    S.append("Целевая функция T(" + str(k) + ")G алгоритма: " + str(format(r7, '.4f')))
    S.append("Целевая функция CTG(k=" + str(k2) + ") алгоритма: " + str(format(r8, '.4f')))
    S.append("Целевая функция Gk(k=" + str(k3) + ") алгоритма: " + str(format(r9, '.4f')))

    plt.rcParams["figure.figsize"] = 10, 10
    ax1 = plt.subplot(2, 1, 1)
    ax2 = plt.subplot(2, 1, 2)

    # ax1.set_title("Сравнение алгоритмов")
    # ax1.set_xlabel("Число партий")
    # ax1.set_ylabel("S")
    # ax1.plot(Days, res1, linestyle = '-', color = 'black', label = "Венгерский мин")
    # ax1.plot(Days, res2, linestyle = '-', color = 'purple', label = "Венгерский макс")
    # ax1.plot(Days, res3, linestyle = '-', color = 'green', label = "Жадный")
    # ax1.plot(Days, res4, linestyle = '-', color = 'red', label = "Бережливый")
    # ax1.plot(Days, res5, linestyle = '-', color = 'blue', label = "Жадно-бережливый")
    # ax1.plot(Days, res6, linestyle = '-', color = 'brown', label = "Бережливо-жадный")
    # ax1.plot(Days, res7, linestyle='--', color='grey', label="T(k)G")
    # ax1.plot(Days, res8, linestyle='--', color='green', label="CTG")
    # ax1.plot(Days, res9, linestyle='--', color='red', label="Gk")
    # ax1.legend()
    # plt.show()

    m2 = [0 for i in range(n)]
    m1 = [abs(res2[i] - res1[i]) / res1[i] for i in range(n)]
    m3 = [abs(res2[i] - res3[i]) / res3[i] for i in range(n)]
    m4 = [abs(res2[i] - res4[i]) / res4[i] for i in range(n)]
    m5 = [abs(res2[i] - res5[i]) / res5[i] for i in range(n)]
    m6 = [abs(res2[i] - res6[i]) / res6[i] for i in range(n)]
    m7 = [abs(res2[i] - res7[i]) / res7[i] for i in range(n)]
    m8 = [abs(res2[i] - res8[i]) / res8[i] for i in range(n)]
    m9 = [abs(res2[i] - res9[i]) / res9[i] for i in range(n)]

    # ax2.set_title("Сравнение ошибок")
    # ax2.set_xlabel("Число партий")
    # ax2.set_ylabel("Ошибка")
    # ax2.plot(Days, m1, linestyle = '-', color = 'black', label = "Венгерский мин")
    # ax2.plot(Days, m2, linestyle = '-', color = 'purple', label = "Венгерский макс")
    # ax2.plot(Days, m3, linestyle = '-', color = 'green', label = "Жадный")
    # ax2.plot(Days, m4, linestyle = '-', color = 'red', label = "Бережливый")
    # ax2.plot(Days, m5, linestyle = '-', color = 'blue', label = "Жадно-бережливый")
    # ax2.plot(Days, m6, linestyle = '-', color = 'brown', label = "Бережливо-жадный")
    # ax2.legend()
    # plt.show()

    return S, [res1, res2, res3, res4, res5, res6, res7, res8, res9]

def manual(n, mu, matrix):
    Days = [i + 1 for i in range(n)]
    r1, indices1, res1 = sb.hungarian_min(matrix)
    r2, indices2, res2 = sb.hungarian_max(matrix)
    r3, indices3, res3 = sb.greedy(matrix)
    r4, indices4, res4 = sb.thrifty(matrix)
    r5, indices5, res5 = sb.greedy_thrifty(matrix, mu)
    r6, indices6, res6 = sb.thrifty_greedy(matrix, mu)
    r7, indices7, res7 = sb.TkG(matrix, mu, 1)
    k = 1
    for i in range(1, n // 2):
        r, ind, res = sb.TkG(matrix, mu, i)
        if (r7 < r):
            r7 = r
            indices7 = ind
            res7 = res
            k = i

    r8, indices8, res8 = sb.CTG(matrix, mu, 1)
    k2 = 1
    for i in range(1, n):
        r, ind, res = sb.CTG(matrix, mu, i)
        if (r8 < r):
            r8 = r
            indices8 = ind
            res8 = res
            k2 = i

    r9, indices9, res9 = sb.Gk(matrix, mu, 4)
    k3 = 1
    for i in range(1, n):
        r, ind, res = sb.Gk(matrix, mu, i)
        if (r9 < r):
            r9 = r
            indices9 = ind
            res9 = res
            k3 = i

    S = []

    # print('\n')
    S.append("Целевая функция Венгерского минимума: " + str(format(r1, '.4f')))
    S.append("Целевая функция Венгерского максимума: " + str(format(r2, '.4f')))
    S.append("Целевая функция Жадного алгоритма: " + str(format(r3, '.4f')))
    S.append("Целевая функция Бережливого алгоритма: " + str(format(r4, '.4f')))
    S.append("Целевая функция Жадно-бережливого алгоритма: " + str(format(r5, '.4f')))
    S.append("Целевая функция Бережливо-жадного алгоритма: " + str(format(r6, '.4f')))
    S.append("Целевая функция T(" + str(k) + ")G алгоритма: " + str(format(r7, '.4f')))
    S.append("Целевая функция CTG(k=" + str(k2) + ") алгоритма: " + str(format(r8, '.4f')))
    S.append("Целевая функция Gk(k=" + str(k3) + ") алгоритма: " + str(format(r9, '.4f')))

    # plt.rcParams["figure.figsize"] = 10, 10
    # ax1 = plt.subplot(2, 1, 1)
    # ax2 = plt.subplot(2, 1, 2)

    # ax1.set_title("Сравнение алгоритмов")
    # ax1.set_xlabel("Число партий")
    # ax1.set_ylabel("S")
    # ax1.plot(Days, res1, linestyle = '-', color = 'black', label = "Венгерский мин")
    # ax1.plot(Days, res2, linestyle = '-', color = 'purple', label = "Венгерский макс")
    # ax1.plot(Days, res3, linestyle = '-', color = 'green', label = "Жадный")
    # ax1.plot(Days, res4, linestyle = '-', color = 'red', label = "Бережливый")
    # ax1.plot(Days, res5, linestyle = '-', color = 'blue', label = "Жадно-бережливый")
    # ax1.plot(Days, res6, linestyle = '-', color = 'brown', label = "Бережливо-жадный")
    # ax1.legend()
    # plt.show()

    m2 = [0 for i in range(n)]
    m1 = [abs(res2[i] - res1[i]) / res1[i] for i in range(n)]
    m3 = [abs(res2[i] - res3[i]) / res3[i] for i in range(n)]
    m4 = [abs(res2[i] - res4[i]) / res4[i] for i in range(n)]
    m5 = [abs(res2[i] - res5[i]) / res5[i] for i in range(n)]
    m6 = [abs(res2[i] - res6[i]) / res6[i] for i in range(n)]
    m7 = [abs(res2[i] - res7[i]) / res7[i] for i in range(n)]
    m8 = [abs(res2[i] - res8[i]) / res8[i] for i in range(n)]
    m9 = [abs(res2[i] - res9[i]) / res9[i] for i in range(n)]

    # ax2.set_title("Сравнение ошибок")
    # ax2.set_xlabel("Число партий")
    # ax2.set_ylabel("Ошибка")
    # ax2.plot(Days, m1, linestyle = '-', color = 'black', label = "Венгерский мин")
    # ax2.plot(Days, m2, linestyle = '-', color = 'purple', label = "Венгерский макс")
    # ax2.plot(Days, m3, linestyle = '-', color = 'green', label = "Жадный")
    # ax2.plot(Days, m4, linestyle = '-', color = 'red', label = "Бережливый")
    # ax2.plot(Days, m5, linestyle = '-', color = 'blue', label = "Жадно-бережливый")
    # ax2.plot(Days, m6, linestyle = '-', color = 'brown', label = "Бережливо-жадный")
    # ax2.legend()
    # plt.show()

    return S, [res1, res2, res3, res4, res5, res6, res7, res8, res9]

# experiment(50, 0.2, 0.5, 1.03, 1.2, 0.95, 0.81)
