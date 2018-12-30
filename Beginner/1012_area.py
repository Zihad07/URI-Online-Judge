"""
input:
3.0 4.0 5.2

output:
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000
"""

# input 3 flaoting value form user 

a, b, c = map(float, input().split())

pi = 3.14159
triangle_area = 0.5 * a * c
circle_area = pi * c**2
trapezium_area = (a + b) * c * 0.5
squre_area = b**2
rectangle_area = a * b

print("TRIANGULO: %0.3f" %triangle_area)
print("CIRCULO: %0.3f" %circle_area)
print("TRAPEZIO: %0.3f" %trapezium_area)
print("QUADRADO: %0.3f" %squre_area)
print("RETANGULO: %0.3f" %rectangle_area)