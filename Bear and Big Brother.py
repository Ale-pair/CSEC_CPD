def years_until_larger(a, b):
    years = 0
    while a <= b:
        a *= 3  # Limak's weight triples
        b *= 2  # Bob's weight doubles
        years += 1
    return years

# Reading input
a, b = map(int, input().split())

# Calculate the result and print it
print(years_until_larger(a, b))
