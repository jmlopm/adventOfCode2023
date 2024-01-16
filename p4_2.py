def points(w,a):
    ret=0
    for n in w:
        if n in a:
            ret+=1
    return ret

f=open("input")
res=0
mult={}
ident=1
for l in f:
    arr1=l.replace("\n","").split(":")[1].split("|")
    w=arr1[0].split(" ")
    winning=set([int(a) for a in w if a!=""])
    a=arr1[1].split(" ")
    a.remove("")
    appearing=set([int(b) for b in a if b!=""])
    aux=points(winning,appearing)
    if not ident in mult:
        mult[ident]=1
    else:
        mult[ident]+=1
    for i in range(0,aux):
        if (ident+i+1) in mult:
            mult[ident+i+1]+=mult[ident]
        else:
            mult[ident+i+1]=mult[ident]
    #res+=aux*mult[ident]
    #print(res,mult)
    ident+=1

print(sum([mult[a] for a in mult]))    


f.close()
