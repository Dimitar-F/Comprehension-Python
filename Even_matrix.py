n = int(input())

matrix = (
    [map(int, input().split(', ')) for row in range(n)]
)

even_matrix = (
    [[x for x in row if x % 2 == 0] for row in matrix]
)

print(even_matrix)