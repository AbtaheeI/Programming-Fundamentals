words   = ["apple","Banana","kiwi","Cherry"]
nums    = [3,-1,4,-1,5]
weights = [10,20,30,40,50]

# Multiply them element-wise into a new list
# Zip words and nums — explain what the length difference does
# Build a dict from words and nums
# Iterate words and nums together with an index

# Question 1
# for i, x in enumerate(words):
#     print(f"{i} : {x}")

# Question 2
# for i, x in enumerate(words, start= 1):
#      print(f"{i} : {x}")

# Question 3
# empty_list = []
# for i, x in enumerate(words):
#     empty_list.append((i, x))
# print(empty_list)

# Qeustion 4
# tuples = tuple(zip(nums, weights))
# print(tuples)

# Question 5
for i, x in zip(words, nums):
    print(i * x)

