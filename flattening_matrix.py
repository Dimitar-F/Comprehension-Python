n = int(input())

matrix = (
    [input().split(', ') for row in range(n)]
)

flattened = (
    [int(x) for row in matrix for x in row]
)

print(flattened)