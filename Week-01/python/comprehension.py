# Question 1
# squares = [n ** 2 for n in range(1, 21) if n % 2 != 0]

# Question 2
# words = ["apple","Banana","kiwi","Cherry"]
# words_lower_case = [n.lower() for n in words]

# Questions 3
# words = ["apple","Banana","kiwi","Cherry"]
# length_filter = [n for n in words if len(n) > 4]

# Question 4(Not Done)
# words = ["apple","Banana","kiwi","Cherry"]
# tuple_words = tuple((n, len(n)) for n in words)

# Question 5
# nums = [3,-1,4,-1,5,-9,2]
# positive_nums = [ 0 if n < 0 else n for n in nums]

# Question 6
# nums = [3,-1,4,-1,5,-9,2]
# descending_nums = sorted([abs(n) for n in nums], reverse = True)

# Question 7
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# flattened_matrix = [x for row in matrix for x in wor]

# Question 8
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# sum_rows_matrix = [sum(n) for n in matrix]

# Question 9
# sentence = "the quick brown fox jumps"
# first_letter_in_sentence = [n[0] for n in sentence.split()]

# Question 10
# fizzy = ["FizzBuzz" if n % 3 == 0 and n % 5 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else "n" for n in range(1, 101)]

# Question 11
# words = ["apple","Banana","kiwi","Cherry"]
# words_dict = {n : len(n) for n in words}

# Question 12 (no idea)
# words = ["apple","Banana","kiwi","Cherry"]
# words_dict = {len(n): n for n in words}

# Question 13
# nums = [3,-1,4,-1,5,-9,2]
# nums_set = {abs(n) for n in nums}

# Question 14
# dictionary = {"a":1,"b":2} 
# reverse_dict = {value: key for key, value in dictionary.items()}

# Question 15
# prices = {"apple":1.2,"kiwi":0.8,"cherry":4.0}
# prices_filtering = {key : value for key, value in prices.items() if value < 2}

# Question 16
# 1. list of the squares of even numbers under 30
# nums = [x ** 2 for x in range(1, 30) if x % 2 == 0]
# print(nums)

# Question 17
# 2. dict mapping each word in a sentence to its length, only words > 3 chars
# sentence = "the quick brown fox jumps"
# sentence_dict = {n: len(n) for n in sentence.split() if len(n) > 3}

# Question 18
# matrices = [[1,2],[3,4],[5,6]] 
# flat = [x for n in matrices for x in n]

# Question 19
# words = ["apple","Banana","kiwi","Cherry"]
# words_list = ["long" if len(n) > 4 else "short" for n in words]
# print(words_list)