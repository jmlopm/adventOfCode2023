colors=["blue","red","green"]

def isPossible(m):
    return m["blue"]<=14 and m["green"]<=13 and m["red"]<=12



def analizeLine(l):
    arr1=l.split(":")
    gameId=int(arr1[0].split(" ")[1])
    sets=arr1[1].split(";")
    ret={}
    for s in sets:
        arr2=s.split(",")
        for ball in arr2:
            b2=ball.split(" ")
            if b2[2] not in colors:
                return 0
            if b2[2] in ret:
                ret[b2[2]]=max(ret[b2[2]],int(b2[1]))
            else:
                ret[b2[2]]=int(b2[1])
    if not "blue" in ret:
        ret["blue"]=0
    elif not "red" in ret:
        ret["red"]=0
    elif not "green" in ret:
        ret["green"]=0
    if isPossible(ret):
        return gameId
    else:
        return 0

res=0
f=open("input")
for l in f:
   res+=analizeLine(l.replace("\n",""))
print(res)
    
