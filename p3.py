def issymbol(c):
    return not c.isnumeric() and not c.isalpha() and not c=="."

def analize(arr, i, j):
    x=[1,0,-1]
    y=[1,0,-1]
    for i2 in x:
        for j2 in y:
            if i+i2<len(arr) and j+j2<len(arr[0])and i+i2>=0 and j+j2>=0:
                if issymbol(arr[i+i2][j+j2]):
                    return True
    return False


def solve(arr):
    ret=0
    i=0
    while i<len(arr):
        j=0
        while j<len(arr[0]):
            if arr[i][j].isnumeric():
                partn=False
                n=int(arr[i][j])
                if analize(arr,i,j):
                    partn=True
                while j+1 < len(arr[0]) and arr[i][j+1].isnumeric():
                    n*=10
                    n+=int(arr[i][j+1])
                    j+=1
                    if analize(arr,i,j):
                        partn=True
                j+=1
                if partn:
                    ret+=n
            else:
                j+=1
        i+=1
    return ret

f=open("input")
arr=[]
for l in f:
    arr.append(l.replace("\n",""))
print(solve(arr))
                
