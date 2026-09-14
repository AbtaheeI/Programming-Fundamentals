nums = [1,0,1,1]
k = 1

# Version 1 of optimised version
# numbers = {}
# for index, value in enumerate(nums):
#     numbers[value] = numbers.get(value, index)
#     if value in numbers:
#         print(numbers[value], index)
#         if abs(numbers[value] - index) <= k:
#             print(True)
# print(False)


# Version 2 of optimised verion
# numbers = {}
# for index, value in enumerate(nums):
#     if value in numbers:
#         numbers[value] = index
#         print(numbers[value], index)
#         if abs(numbers[value] - index) <= k:
#             print(True)
#     numbers[value] = numbers.get(value, index)
# print(False)


# Actual solution
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         numbers = {}
#         for index, value in enumerate(nums):
#             if value in numbers and abs(numbers[value] - index) <= k:
#                     return True
#             numbers[value] = index
#         return False
        