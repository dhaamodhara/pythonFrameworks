def isnum(s):
    for i in s:
        if i>='0' and i<='9':
            continue
        return False
    return True
print(isnum('123'))