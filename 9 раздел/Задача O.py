# Циклически сдвиньте элементы списка вправо# (A[0] переходит на место A[1],# A[1] на место A[2], ...,# последний элемент переходит на место A[0]).

l = list(map(int, input().split()))


a = l[-1:] + l[:-1]


for i in range(len(a)):
    print(a[i], end=' ')
