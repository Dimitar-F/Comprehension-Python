vowels = ['a', 'o', 'u', 'e', 'i']
word = input()

result = []
comprehension = (
    [result.append(ch) for ch in word if ch not in vowels]
)

print(''.join(result))
