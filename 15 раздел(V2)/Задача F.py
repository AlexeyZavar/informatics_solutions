# ������ �111331. ������� ������
# � �������� ���� �������� ��� ������ ���������� ����� �� �������� �����, �� ����� �� �������.
# � ������ ������ ������ ������� ������ ����� �������� ����� ������� ���
# ������ ������ readlines().

fil = open('input.txt', 'r')
file = fil.readlines()
i = 0
AA = []
fuck = -1

for item in file:
    gg = len(item)
    if gg >= fuck:
        fuck = gg

for item in file:
    gg = len(item)
    if gg == fuck:
        AA.append(item)

print(*AA, sep='')
