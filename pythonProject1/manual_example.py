import algorithms_sugarbeet as sb
import matplotlib.pyplot as plt

n = int(input())

matrix = []

for i in range(0, n):
    vector = []
    for j in range(0, n):
        vector.append(float(input()))
    matrix.append(vector)

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

#print("Венг. мин: ", r1, "\nВенг. макс: ", r2, "\nЖадный: ", r3)
print("\nВенг. мин: ", indices1, "\nВенг. макс: ", indices2, "\nЖадный: ", indices3,
      "\nБережливый: ", indices4, "\nЖадно-бережливый: ", indices5, "\nБережливо-жадный: ", indices6)