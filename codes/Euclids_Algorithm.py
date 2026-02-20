def hcf(a,b):
    if(a<b):
        a, b = b, a
    if(b == 0):
        return a
    return hcf(b,a%b)

#=================================================
#=================================================
a = int(input())
b = int(input())
print(hcf(a,b))
