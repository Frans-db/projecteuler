with open('problem11.txt') as f:
    data = f.read()

grid = [d.split(' ') for d in data.split('\n')]
for row in grid:
    for i in range(len(row)):
        row[i] = int(row[i])

width = len(grid[0])
height = len(grid)

def find_max_row(grid, n):
    max_product = 0
    max_sum = 0
    max_values = []
    for row in grid:
        for i in range(width - n + 1):
            cur_product = 1
            cur_sum = 0
            values = []
            for j in range(n):
                cur_product *= row[i+j]
                values.append(row[i+j])
                cur_sum += row[i+j]
            max_product = max(max_product, cur_product)
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_values = values
    print(max_values)
    return max_product

def find_max_column(grid, n):
    max_product = 0
    max_sum = 0
    max_values = []
    for i in range(width):
        for j in range(height-n+1):
            cur_product = 1
            cur_sum = 0
            values = []
            for k in range(n):
                values.append(grid[j+k][i])
                cur_product *= grid[j+k][i]
                cur_sum += grid[j+k][i]
            max_product = max(max_product, cur_product)
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_values = values
    print(max_values)
    return max_product

def find_max_diagonal(grid, n):
    max_product = 0
    for i in range(height-n+1):
        for j in range(width-n+1):
            cur_product = 1
            for k in range(n):
                cur_product *= grid[i+k][j+k]
            max_product = max(max_product, cur_product)
    
    for i in range(height-n+1):
        for j in range(width-n+1):
            cur_product = 1
            values = []
            for k in range(n):
                cur_product *= grid[height-i-k-1][width-j-k-1]
                values.append(grid[height-i-k-1][width-j-k-1])
            print(cur_product, values)
            max_product = max(max_product, cur_product)

    return max_product

for row in grid:
    print(row)
print(find_max_row(grid, 4))
print(find_max_column(grid, 4))
print(find_max_diagonal(grid, 4))