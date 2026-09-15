nums = [6, 5, 5]
count = 0
majority_element_currently = nums[0]
for i in range(len(nums)):

    if nums[i] != majority_element_currently:
        count -= 1
    else:
        count += 1
    print(majority_element_currently)
#print(majority_element_currently)