def getFirst(s):
    for c in s:
        if c.isnumeric():
            return int(c)
        
def getLast(s):
    for c in s[::-1]:
        if c.isnumeric():
            return int(c)

f=open("input")

res=0


for l in f: 
    res+=10*getFirst(l)+getLast(l)
print(res)
