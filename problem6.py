total_sum = 0
total_squared = 0
for i in range(101):
    total_sum += i
    total_squared += i**2
total_sum = total_sum**2
print(total_sum, total_squared)
print(total_sum - total_squared)