# А вот другой ряд, в котором вычисляется значение дзета-функции для числа 2
# Вычислите приближение к числу , используя первые 10 членов этого ряда.

terms = 10

a = 0
for i in range(1, terms+1):
    a += 1 / i ** 2
b = (6 * a)**(1/2)
print(b)
