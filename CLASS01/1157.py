ALPHABET_TOTAL = 26
CAPITAL_DIFF = 32

word = input()

count = [0 for i in range(ALPHABET_TOTAL)]

for alp in word:
    if ord('A') <= ord(alp) <= ord('Z'):
        index = ord(alp) + 32
        count[index - ord('a')] = count[index - ord('a')] + 1
    else:
        count[ord(alp) - ord('a')] = count[ord(alp) - ord('a')] + 1

maxCount = max(count)

if count.count(maxCount) != 1:
    print('?')
else:
    print(chr(count.index(maxCount) + ord('a') - 32))
