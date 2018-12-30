"""
input:
12 1 5.30
16 2 5.10

output:
VALOR A PAGAR: R$ 15.50
"""

# For prduct - 1
id_1, unit_1, unint_price_1 = map(float, input().split())

# For prduct - 2
id_2, unit_2, unint_price_2 = map(float, input().split())

total_price = (unit_1*unint_price_1) + (unit_2*unint_price_2)

print("VALOR A PAGAR: R$ %0.2f" % total_price)
