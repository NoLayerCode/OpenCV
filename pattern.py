n = int(input())

# generate the top half of the design
for i in range(n // 2, -1, -1):
    row = "-" * (i * 2) + "*|" + "**|" * ((n // 2) - i) + "*" * (n * 3 - (i * 2 + 4) * 2) + "|**|" * ((n // 2) - i) + "-" * (i * 2)
    print(row)

# print the center design
center_row = "-" * ((n // 2) * 2) + "*" * (n * 3 - (n // 2) * 4) + "SCSDF" + "*" * (n * 3 - (n // 2) * 4) + "-" * ((n // 2) * 2)
print(center_row)

# generate the bottom half of the design
for i in range(1, n // 2 + 1):
    row = "-" * (i * 2) + "*|" + "**|" * ((n // 2) - i + 1) + "*" * (n * 3 - (i * 2 + 4) * 2) + "|**|" * ((n // 2) - i + 1) + "-" * (i * 2)
    print(row)
