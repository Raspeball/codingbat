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
#
#
#
#  rotate_left3 #
'''Given an array of ints length 3, return an array with the elements
"rotated left" so {1, 2, 3} yields {2, 3, 1}.'''

def rotate_left3(nums):
    res = [nums[-len(nums) + 1 + i] for i, val in enumerate(nums)]
    return res
#
#
#
#  has23 #
'''Given an int array length 2, return True if it contains a 2 or a 3.'''

def has23(nums):
  return (2 in nums or 3 in nums)
#
#
#
#  sum2 #
'''Given an array of ints, return the sum of the first 2 elements in the array.
If the array length is less than 2, just sum up the elements that exist,
returning 0 if the array is length 0.'''

def sum2(nums):
    if len(nums) < 2:
        return sum(nums)
    else:
        return sum(nums[0:2])
