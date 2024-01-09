def issymbol(c):
    return not c.isnumeric() and not c.isalpha() and not c=="."

def analize(arr, i, j):
    x=[1,0,-1]
    y=[1,0,-1]
    for i2 in x:
        for j2 in y:
            if i+i2<len(arr) and j+j2<len(arr[0]):
                if issymbol(arr[i+i2][j+j2]):
                    return True
    return False

def getHash(i,j,n):
    return i*n+j

def getnumber(arr, i , j, marcas):
    ret=0
    j2=j
    while j2>=0 and arr[i][j2].isnumeric():
        j2-=1
    ret=int(arr[i][j2+1])
    j2+=1
    marcas[i*len(arr)+j2+1]=True
    while  j2+1<len(arr[i]) and arr[i][j2+1].isnumeric():
        ret*=10
        ret+=int(arr[i][j2+1])
        marcas[i*len(arr[0])+j2+1]=True
        j2+=1
    #print(ret)
    return ret
    

def getgearratio(c,arr,i,j,marcas):
    if c!="*":
        return 0
    ret=1
    count=0
    if i-1>=0 and j-1>=0:
        if arr[i-1][j-1].isnumeric() and not getHash(i-1,j-1,len(arr)) in marcas:
            count+=1
            ret*=getnumber(arr,i-1,j-1,marcas)
    if i-1>=0:
        if arr[i-1][j].isnumeric() and not getHash(i-1,j,len(arr)) in marcas:
            count+=1
            ret*=getnumber(arr,i-1,j,marcas)
    if i-1>=0 and j+1<len(arr[i-1]):
        if arr[i-1][j+1].isnumeric() and not getHash(i-1,j+1,len(arr)) in marcas:
            count+=1
            ret*=getnumber(arr,i-1,j+1,marcas)
    if j-1>=0:
        if arr[i][j-1].isnumeric() and not getHash(i,j-1,len(arr)) in marcas:
            count+=1
            ret*=getnumber(arr,i,j-1,marcas)
    if j+1<len(arr[i]):
        if arr[i][j+1].isnumeric() and not getHash(i,j+1,len(arr)) in marcas:
            count+=1
            ret*=getnumber(arr,i,j+1,marcas)
    if i+1<len(arr) and j-1>=0:
        if arr[i+1][j-1].isnumeric() and not getHash(i+1,j-1,len(arr)) in marcas:
            count+=1
            ret*=getnumber(arr,i+1,j-1,marcas)
    if i+1<len(arr):
        if arr[i+1][j].isnumeric() and not getHash(i+1,j,len(arr)) in marcas:
            count+=1
            ret*=getnumber(arr,i+1,j,marcas)
    if i+1<len(arr) and j+1<len(arr[i+1]):
        if arr[i+1][j+1].isnumeric() and not getHash(i+1,j+1,len(arr)) in marcas:
            count+=1
            ret*=getnumber(arr,i+1,j+1,marcas)
    #print(count,ret)
    if count==2:
        return ret
    else:
        return 0

def solve(arr):
    ret=0
    i=0
    marcas={}
    while i<len(arr):
        j=0
        while j<len(arr[0]):
            if arr[i][j]=="*":
                ret+=getgearratio(arr[i][j],arr,i,j,marcas)
            j+=1
        i+=1
    return ret

f=open("input")
arr=[]
for l in f:
    arr.append(l.replace("\n",""))
print(solve(arr))
f.close()
                
