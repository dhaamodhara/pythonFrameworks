
def startswith(sub,s,start=0,end=0):
    if end==0:
        end=len(s)
    if start+len(sub)<=end and s[start:start+len(sub)]==sub:
        return True
    return False
print(startswith('h','hello'))
print(startswith('he','hello',0,1))
print(startswith('he','hello',0,2))