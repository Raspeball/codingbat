## https://codingbat.com/python/String-1 ##
# all string-1 problems in one file #
#
#
#
# reverse3 #
'''Given an array of ints length 3, return a new array with the elements in
reverse order, so {1, 2, 3} becomes {3, 2, 1}.'''

# built-in solution
def reverse3(nums):
    return list(reversed(nums))

# listing-solution
def reverse3_2(nums):
    rev = [nums[len(nums) - i - 1] for i, j in enumerate(nums)]

    return rev
#
#
#
#  same_first_Last #
'''Given an array of ints, return True if the array is length 1 or more,
and the first element and the last element are equal.'''

def same_first_last(nums):
    return (len(nums) >= 1 and nums[0] == nums[-1])
