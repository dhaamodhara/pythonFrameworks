def endswith(sub,s,start=0,end=0):
    if end==0:
        end=len(s)
    if end-start>=len(sub) and s[end-len(sub):end]==sub:
        return True
    return False
print(endswith('o','hello'))
print(endswith('lo','hello'))
print(endswith('h','hello'))