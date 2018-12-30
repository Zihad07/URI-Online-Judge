"""
input:
3

output:
VOLUME = 113.097
"""

pi = 3.14159

radius = float(input())

sphere = (4/3) * pi * radius**3
print("VOLUME = %0.3f" % sphere)