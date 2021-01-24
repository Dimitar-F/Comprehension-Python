
start = int(input())
end = int(input())


def is_valid(i):
    return any(i % x == 0 for x in range(2, 11))


print(
    [i for i in range(start, end+1) if is_valid(i)]
)