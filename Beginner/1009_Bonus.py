
"""
input:
JOAO
500.00
1230.30

output:
TOTAL = R$ 684.54
"""

emp_name = input()
fixed_salary = float(input())
sold_product = float(input())
# 15% over all product sold

commison = sold_product * 0.15 # 15%

print("TOTAL = R$ %0.2f" % (commison+fixed_salary))