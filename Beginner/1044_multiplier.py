
a, b = map(int, input().split())

max_value = max(a,b)
min_value = min(a,b)

if( not max_value % min_value ):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")