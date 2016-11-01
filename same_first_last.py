
# Given an array of ints, return True if the array is length 1 or more,
# and the first element and the last element are equal.

# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True

def same_first_last(nums):
    if (len(nums) >= 1) and (nums[0] == nums[-1]):
        return True
    else:
        return False

print(same_first_last([1, 2, 3])) #→ False
print(same_first_last([1, 2, 3, 1])) #→ True
print(same_first_last([1, 2, 1])) #→ True
print(same_first_last([7])) #→ True
print(same_first_last([])) #→ False
print(same_first_last([1, 2, 3, 4, 5, 1])) #→ True
print(same_first_last([1, 2, 3, 4, 5, 13])) #→ False
print(same_first_last([13, 2, 3, 4, 5, 13])) #→ True
print(same_first_last([7, 7])) #→ True