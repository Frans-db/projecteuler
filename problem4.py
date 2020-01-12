largest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product_int = i * j
        product_str = str(product_int)
        if product_str == product_str[::-1] and product_int > largest:
            largest = product_int
print(largest)