def points(w,a):
    ret=0.5
    for n in w:
        if n in a:
            ret*=2
    if ret<1:
        return 0
    else:
        return ret
    
            



f=open("input")
res=0

for l in f:
    arr1=l.replace("\n","").split(":")[1].split("|")
    w=arr1[0].split(" ")
    winning=set([int(a) for a in w if a!=""])
    a=arr1[1].split(" ")
    a.remove("")
    appearing=set([int(b) for b in a if b!=""])
    res+=points(winning,appearing)
    


print(res)
f.close()
