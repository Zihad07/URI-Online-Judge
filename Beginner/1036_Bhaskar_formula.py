
# ax^2 + bx + c =0
# root value r1, r2
# discriment D = b^2 - 4ac
import math
a, b, c = map(float, input().split())

D = b**2 - 4*a*c

if a == 0 or D<0:
    print("Impossivel calcular")
else:
    b = -b
    r1 =  (b+math.sqrt(D)) / (2*a)
    r2 = (b-math.sqrt(D)) / (2*a)
    #output
    print("R1 = %0.5f" % r1)
    print("R2 = %0.5f" % r2)