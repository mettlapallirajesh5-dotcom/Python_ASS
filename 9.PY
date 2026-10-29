# Case Study 9: Tuple-Based Product Catalogue Audit

products = (
    ("Laptop", 50000, 5),
    ("Mouse", 500, 3),
    ("Keyboard", 1500, 10),
    ("Headphones", 2000, 2)
)

total_value = 0

print("Product Catalogue Report")
print("------------------------")

for name, price, quantity in products:
    value = price * quantity
    total_value += value

    print("Product:", name)
    print("Price: Rs.", price)
    print("Quantity:", quantity)
    print("Stock Value: Rs.", value)

    if quantity < 5:
        print("Status: Low Stock")
    else:
        print("Status: Sufficient Stock")

    print()

print("Total Catalogue Value: Rs.", total_value)