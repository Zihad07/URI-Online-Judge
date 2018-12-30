"""
input
7 14 106

output:
106 eh o maior
"""


def maxValue (v1,v2):
    if(v1<=v2):
        return v2
    return v1

a,b,c = map(int, input().split())

maxvalue = maxValue(maxValue(a,b),c)

print(str(maxvalue)+" eh o maior")