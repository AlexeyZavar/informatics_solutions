# ������ �111343. ��� ���������� ��-����������
# � �������� ���������� ������ �������� ������� � ��� ��������� ���������,
# ���������� ���������� ����, �� �� �������� �����������. ���� �����
# ���������� ��������� - �������� �� ����������.

import collections
fil = open('input.txt', 'r')
file = fil.readlines()
A, AA = [], []
F = []

for item in file:
    A.append(item.split())

for i in range(len(file)):
    last_name, first_name, class_number, points = map(
        str, file[i].replace('\n', '').split())
    F.append(int(points))

f = max(F)

for i in range(F.count(f)):
    F.remove(f)

max1 = max(F)

cheat = F.count(max1)

j = 0

if cheat == 1:
    for j in range(len(A)):
        if str(max1) in A[j]:
            print(A[j][0], A[j][1])
        else:
            j += 1
else:
    print(cheat)
# A[i][3]
