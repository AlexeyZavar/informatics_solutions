# Дана строка, возможно, содержащая пробелы. Определите, является ли эта строка палиндромом, при условии, что заглавные и строчные буквы не различаются, а все символы, не являющиеся буквами, должны быть пропущены. Выведите слово YES, если слово является палиндромом и слово NO, если не является.
#    

text = input()


def Palynd(s):
    b = ''
    for i in range(len(s)):
        if s[i].isalpha():
            b += s[i].lower()
    if b == b[::-1]:
        return True
    else:
        return False


if Palynd(text):
    print('YES')
else:
    print('NO')
