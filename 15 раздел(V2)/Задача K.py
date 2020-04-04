# ������ �111336. ���� ������ - 2
# ���������� ������ ��������� ���� ������ ������, ��� ���� ������� ������ ������ ����� ������ ���������� ���������� �� 1, ������ ������ � �� 2, ������� ������ � �� ��� � �.�.
# � ���� ������ ������ ��������� ���� ���������, ������ ������ ������ �
# �����������.

import re

i = 0

fil = open('input.txt', 'r').readlines()

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def CaesarCipherChar(c, k):
    d = alphabet.find(c.lower())
    l = len(alphabet) // 2
    if d < l and c in alphabet:
        l *= 2
        if c.islower():
            return alphabet[(d + k) % len(alphabet)].lower()
        else:
            return alphabet[(d + k) % len(alphabet)].upper()
    elif c not in alphabet:
        return c
    if c.islower():
        return alphabet[d + k - l].lower()
    else:
        return alphabet[d + k - l].upper()


def CaesarCipher(s, k):
    for item in s:
        yield CaesarCipherChar(item, k)


for item in fil:
    i += 1
    print(*CaesarCipher(item[:-1], i), sep='')
