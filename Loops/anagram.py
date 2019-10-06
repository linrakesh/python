# program to find out all anagram of given word
# made by       : rakesh kumar

from itertools import permutations

def words(letters):
    yield from map(''.join, permutations(letters, len(letters)))

result = set()
for word in words('Compute'):
    result.add(word)

print(f' There are {len(result)} combinations')
print(result)


