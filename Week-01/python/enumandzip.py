words   = ["apple","Banana","kiwi","Cherry"]
nums    = [3,-1,4,-1,5]
weights = [10,20,30,40,50]

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
# output = []
# for num, weight in zip(nums, weights):
#     output.append(num * weight)

# Question 6
# idk

# Question 7
# dictionary = {word: num for word, num in zip(words, nums)}

# Question 8
for i in range(zip(words, nums)):
    print(words[i])
    print(nums[i])
