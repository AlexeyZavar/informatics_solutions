# ������ �111342. ������������ ���� ������� � �� ����������
# ���������� ��������� ���������� ��� ������� �� ������. ����������� ��������� ���������� ��, ��� ������ ������ ����� ������. ��������� ��������� ���������� ���������, ��������� �� ������������.
# ���������� ���������� ����, ������� ������� ������� ��������� �
# ���������� ���������� ���������, ��������� ����� ����.

import collections
fil = open('input.txt', 'r')
file = fil.readlines()
A = []
for i in range(len(file)):
    last_name, first_name, class_number, points = map(
        str, file[i].replace('\n', '').split())
    A.append(int(points))

a1 = max(A)

for i in range(A.count(a1)):
    A.remove(a1)
print(max(A), A.count(max(A)))
