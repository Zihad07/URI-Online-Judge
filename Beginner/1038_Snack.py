
# product price

prduct_code_price = {
    1 : 4.0,
    2 : 4.50,
    3 : 5.00,
    4 : 2.00,
    5 : 1.50
}

code, quantity = map(int, input().split())

price = prduct_code_price[code] * quantity;

print("Total: R$ %0.2f" %price)