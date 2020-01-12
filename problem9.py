def triplet(n):
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if a + b + c == n and a**2 + b**2 == c**2:
                    return a * b * c

print(triplet(1000))