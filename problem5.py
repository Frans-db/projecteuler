import math

def prime_factors(n):
    factors = {}
    for i in range(2, n):
        while n % i == 0 and n != 0:
            n = n / i
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
    if len(factors) == 0:
        factors[n] = 1
    return factors

def lcm(values):
    all_dicts = []
    max_values = {}
    for i in values:
        all_dicts.append(prime_factors(i))
    for dictionary in all_dicts:
        for k, v in dictionary.items():
            if (k in max_values and v > max_values[k]) or k not in max_values:
                max_values[k] = v
    
    value = 1
    for k, v in max_values.items():
        for i in range(v):
            value *= k
    return value

values = [i for i in range(1, 21)]
value = lcm(values)
print(value)