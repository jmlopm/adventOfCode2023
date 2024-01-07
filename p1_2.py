digits=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def getFirst(s2):
    s=s2+"     "
    for i in range(0, len(s)-5):
        if s[i].isnumeric():
            return int(s[i])
        else:
            for j in range(0, len(digits)):
                if digits[j][0]==s[i]:
                    #print(digits[j], s[i:i+5],s ,i)
                    if digits[j] in s[i:i+5]:
                        return j+1

def getLast(s2):
    s=s2[::-1]+"     "
    for i in range(0, len(s)-5):
        if s[i].isnumeric():
            return int(s[i])
        else:
            for j in range(0, len(digits)):
                if digits[j][::-1][0]==s[i]:
                    #print(digits[j][::-1], s[i:5])
                    if digits[j][::-1] in s[i:i+5]:
                        return j+1

def calibrate(line):
    return 10*getFirst(line)+getLast(line)
  
        

f=open("input")

res=0


for l in f: 
    l=l.replace("\n","")
    l2=l.lower()
    print(calibrate(l2))
    res+=calibrate(l2)
print(res)
