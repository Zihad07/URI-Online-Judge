
a, b, c  = map(float, input().split())

if a+b > c and b+c> a and a+c> b:
    print("Perimetro = %0.1f" %(a+b+c))
else:
    print("Area = %0.1f" %(0.5*(a+b)*c))
