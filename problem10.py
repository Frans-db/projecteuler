from math import ceil

n = 2000000
nums = [i for i in range(n)]
marked = set()

p = 2
new_p = -1
while True:
    for i in range(2, ceil(n/p)):
        marked.add(i * p)
    for i in range(p+1,n):
        if i not in marked:
            new_p = i
            break
    if p == new_p:
        break
    p = new_p

total = 0
for num in nums:
    if num not in marked:
        total += num
print(total - 1)