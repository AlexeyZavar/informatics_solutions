# ������ �111349. ����� � ������� ������� ������
# � �������� ���������� ������ �������� � ������� ����������� ������ ����,
# ������� ���� �������� ������� ����, ��� ������� ���� ���� ����������
# ��������� (�� ���� ���������� ��������� ������� ���� ��� ������ ����� �
# ������� ���� �� ���� ����������).

fil = open('input.txt', 'r')
ans, A, AA, COMPLETE = [], [], [], []
for i in range(100):
    ans.append([0, 0])
h = 0
for line in fil:
    h += 1
    AA.append(int(line.split()[3]))
    line = list(line.split()[2:])
    ans[int(line[0])][0] += int(line[1])
    ans[int(line[0])][1] += 1
A.append(h)
A.append(sum(AA))
score = A[1] / A[0]

for k in range(100):
    if ans[k][1] != 0 and ans[k][0] / ans[k][1] > score:
        print(k, end=' ')
