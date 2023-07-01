def find_duplicates(nums):
    duplicates = []
    
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
        else:
            duplicates.append(abs(num))
    
    return duplicates
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(nums))
