# ������ �111347. ������������� ������ ���������� �� ������
# ������������ ������ ���������� ���������:
# 1) �� �������� ���������� �����.
# 2) ��� ������ �������� ����� - �� ������� � ������������������ �������.
# 3) ��� ����������� ������ � ������� - �� ����� � ������������������ �������.

fil = open('input.txt', 'r', encoding='utf8').readlines()
fil = [fil[i][:-1] if fil[i][-1] == '\n' else fil[i] for i in range(len(fil))]
fil.sort(key=lambda x: (-1 * int(x.split()[3]), x.split()[0], x.split()[1]))
print('\n'.join([
    fil[i].split()[0] + ' ' + fil[i].split()[1] + ' ' + fil[i].split()[3]
    for i in range(len(fil))
]))
