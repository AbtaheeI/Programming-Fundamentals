nums = [0, 1, 3]

output = 0
for index, value in enumerate(nums):
     output ^= index 
     output ^= value
output ^= len(nums)
print(output)