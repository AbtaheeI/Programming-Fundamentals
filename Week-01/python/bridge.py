# Bridge Check
# On [1,2,3,4,5], build a running total using an explicit loop and an accumulator. No comprehension, no itertools.
# On [3,2,2,3], remove every 3 by overwriting in place — one read pointer, one write pointer — and report how many elements remain. No .remove(), no new list, no deletion.

# Question 1
# nums = [1, 2, 3, 4, 5]

# running_total = 0
# result = []

# for n in nums:
#     running_total += n
#     result.append(running_total)

# print(result) 

# Question 2
# ls = [3, 2, 2, 3]
# k = 0
# for i in range(len(ls)):
#     if ls[i] != 3:
#         ls[k] = ls[i]
#         k += 1
# print(ls)   


# Cold Check
# Reverse a list with a slice
# Every second element, starting at index 1
# Print index and value together, counting from 1
# Sort (name, score) tuples by score, highest first
# Zip two lists into a dict

# Question 3 
# ls[::-1]

# Question 4
# ls[1::2]

# Question 5
# for i, x in enumerate(words, start=1):
#     print(f"{i} : {x}")

# Question 6
# sorted(tuple, key = lambda pair: pair[1], reverse = True)

# Question 7
# dict(zip(ls1, ls2))