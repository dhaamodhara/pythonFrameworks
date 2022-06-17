def isalpha(s):
    for i in s:
        if i>='a' and i<='z' or i>='A' and i<='Z':
            continue
        return False
    return True
print(isalpha('2aAa'))
