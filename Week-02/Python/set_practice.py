nums = [3, -1, 4, -1, 5, -9, 2, 3]

def has_duplicates(nums):
    return len(nums) != len(set(nums))

print(has_duplicates(nums))