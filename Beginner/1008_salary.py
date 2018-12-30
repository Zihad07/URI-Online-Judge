employe_no  = int(input())
work_hour = int(input())
payment_per_hour = float(input())

monthly_payment = work_hour * payment_per_hour

"""
NUMBER = 25
SALARY = U$ 550.00
"""

print("NUMBER = %d" %employe_no)
print("SALARY = U$ %0.2f" %monthly_payment)