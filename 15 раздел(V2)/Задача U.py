# ������ �111346. ������������� ������ ���������� �� ��������
# ��������, ��� ������� ���� ���������� � ��������. ��������� � �������� ������ ���� ���������� � �������� ���, ������������ �� ������� � ������������������ �������.
# ��� ������ ���������� �������, ��� ��������� � ��� ����.

import operator

fil = open('input.txt', 'r')

file = fil.readlines()

people = []

for item in file:
    people.append(item.split())


def gag(x):
    return x[0]


people = sorted(people, key=gag)

for item in people:
    print(item[0], item[1], item[3])
