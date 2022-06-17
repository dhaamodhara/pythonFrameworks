def count(s):
    temp = " "
    for i in s:
        if i not in temp:
            temp += str(s.count(i))
            temp += i
    return temp
s = count('AAAABABBC')
print(s)
