# author: YANG CUI
"""
Given a sorted array nums, remove the duplicates in-place such that each element
appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input
array in-place with O(1) extra memory.

Approach: Two Pointers
"""

def removeDuplicates(nums):
    # an in-place algo
    if len(nums) == 0: return
    numberOfUniqueElements = 1
    i = 0
    lastJ = 0
    while i < len(nums):
        j = lastJ
        if nums[j] != nums[i]:
            break
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                numberOfUniqueElements += 1
                lastJ = j
                break
        i += 1
    return numberOfUniqueElements

# print(removeDuplicates([1,1,1,2,2,3,4,5,5]))

