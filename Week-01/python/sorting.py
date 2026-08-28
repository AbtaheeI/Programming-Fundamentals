from operator import itemgetter

pairs  = [("apple",5), ("kiwi",4), ("Banana",6), ("Cherry",6)]
prices = {"apple":1.2, "kiwi":0.8, "cherry":4.0}
words = ["apple","Banana","kiwi","Cherry"]


# Sort words alphabetically, case-insensitively


# Question 1
# print(sorted(pairs, key = lambda pair: pair[1]))

# Question 2
# def get_second_element(pair):
#     return pair[1]
# print(sorted(pairs, key=get_second_element))

# Question 3
# print(sorted(pairs, key = itemgetter(1)))

# Question 4
# print(sorted(pairs, key = lambda pair: pair[1], reverse= True))

# Question 5
# print(sorted(words, key=str.lower))

# Question 6
# print(sorted(pairs, key= lambda pair: (-len(pair[0]), pair[0].lower())))

# Question 7
# print(sorted(prices.items(), key= lambda price: price[1]))