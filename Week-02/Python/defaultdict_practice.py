from collections import defaultdict, deque, Counter

text = "the quick brown fox jumps over the lazy dog the fox"


# Method 1
# count = {}
# for i in text.split():
#     count[i] = count.get(i, 0) + 1 
# print(count)

# Method 2
# count = defaultdict(int)
# for i in text.split():
#     count[i] += 1
# print(count)

# Method 3
# count = Counter(text.split())
# print(count)




count_d = {}
for word in text.split():
    if word[0] not in count_d:
        count_d[word[0]] = []
    count_d[word[0]].append(word)
print(count_d)


# count_dd = defaultdict(list)
# for word in text.split():
#     count_dd[word].append(word)
# print(count_dd)