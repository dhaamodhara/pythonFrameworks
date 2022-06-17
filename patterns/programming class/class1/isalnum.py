def isalnum(s):
    for i in s:
        if i>='a' and i<='z' or i>='A' and i<='Z' or i>='0' and i<='9':
            continue
        return False
    return True
print(isalnum('12asAs'))