def count(key, s):
    c = 0
    for i in s:
        if key == i:
            c += 1
    return c


def elim(s):
    temp = ' '
    for i in range(len(s)):
        if count(s[i], s) != 1:
            temp += s[i]
    return temp


print(elim("hello world"))
