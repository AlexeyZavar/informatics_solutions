# ������ �111335. ���������� �� �����
# ��� ����. ���������� ������� � ��� ���� (���������� ��������), ����, �����. �������� ��� ��������� ����� � �������, ����������� � �������.
# ��� �������� ������ ������� ���� �����������, �� ���� �� ��������
# ������� � ������ ���� ��� ��������� ��� ������.

import re

A = []

lines = 0

fil = open('input.txt', 'r')
file = fil.readlines()

words = re.findall(r"[A-Za-z]+", ' '.join(file))

wordres = re.findall(r"[A-Za-z]+", ' '.join(file))

for item in file:
    lines += 1

for i in range(len(words) - 1):
    words[0] += words[i + 1]

letters = len(words[0])

print('Input file contains:')
print(str(letters) + ' letters')
print(str(len(wordres)) + ' words')
print(str(lines) + ' lines')
