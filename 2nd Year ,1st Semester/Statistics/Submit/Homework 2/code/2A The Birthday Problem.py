def birthday_problem():
    k = 0
    q = 1
    p = 0
    total_days = 365
    while p < 0.5:
        k += 1
        q *= (total_days - k + 1) / total_days
        p = 1 - q
        print(f"k = {k}, q = {q}, p = {p}")
        if p >= 0.5:
            return k

# Find the smallest k for which p >= 0.5
result = birthday_problem()
print(f"The smallest k for which p >= 0.5 is: {result}")
