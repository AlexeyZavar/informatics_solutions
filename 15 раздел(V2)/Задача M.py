# ������ �111338. ������� ���� �� �������
# � �������� ���������� ������ ���������� � �������� ������� �����
# ���������� ��������� � 9 ������, � 10 ������, � 11 ������.

g = 1
d = 1
COMPLETE = []
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
aa = (sum(A) / len(A))
bb = (sum(B) / len(B))
cc = (sum(C) / len(C))
if d == g:
    COMPLETE.append(aa)
    COMPLETE.append(bb)
    COMPLETE.append(cc)
print(*COMPLETE)
