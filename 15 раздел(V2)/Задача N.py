# ������ �111339. ���������� ����������� �� �������
# � �������� ���������� ������ ���������� ���������� ����������, �������
# ������������ � ������ ������. ������������ ����������� ���, ��� ������
# ���������� ����� ������ �� ������� ������. �������������, ��� � ������
# ������ ��� ���� �� ���� ��������.

d = 1
g = 1
fil = open('input.txt', 'r')
file = fil.readlines()
A, B, C = [], [], []
for item in file:
    a = list(item.split())
    if a[2] == '9':
        A.append(int(a[3]))
    elif a[2] == '10':
        B.append(int(a[3]))
    else:
        C.append(int(a[3]))
a1 = max(A)
b1 = max(B)
c1 = max(C)
COMPLETE = []
aa = A.count(a1)
bb = B.count(b1)
cc = C.count(c1)
if d == g:
    COMPLETE.append(aa)
    COMPLETE.append(bb)
    COMPLETE.append(cc)
print(*COMPLETE)
