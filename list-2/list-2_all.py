## https://codingbat.com/python/List-2 ##
# all list-2 problems in one file #
#
#
#
# count_evens #
'''Return the number of even ints in the given array. Note: the % "mod" operator
computes the remainder, e.g. 5 % 2 is 1.'''

def count_evens(nums):
    evens = [i for i in nums if i % 2 == 0]

    return len(evens)
#
#
#
# big_diff #
'''Given an array length 1 or more of ints, return the difference between the
largest and smallest values in the array.
Note: the built-in min(v1, v2) and max(v1, v2) functions return the
smaller or larger of two values.'''

# sort-solution
def big_diff(nums):
    nums.sort()
    return nums[-1] - nums[0]
    # return max(nums) - min(nums)

#
#
#
# centered_average #
'''Return the "centered" average of an array of ints, which we'll say is the mean
average of the values, except ignoring the largest and smallest values
in the array. If there are multiple copies of the smallest value,
ignore just one copy, and likewise for the largest value.
Use int division to produce the final average.
You may assume that the array is length 3 or more.'''

def centered_average(nums):
    nums.sort()
    avg = (sum(nums) - nums[0] - nums[-1])/(len(nums)-2)

    return avg
#
#
#
# sum13 #
'''Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that come
immediately after a 13 also do not count.'''

def sum13(nums):
    if len(nums) < 1:
        s = 0

    else:
        s = 0
        for i, j in enumerate(nums):
            if i == 0:
                if j == 13:
                    continue
                else:
                    s += j
            elif j < 13 and nums[i-1] < 13:
                s += j

    return s
#
#
#
# sum67 #
'''Return the sum of the numbers in the array, except ignore sections of numbers
starting with a 6 and extending to the next 7 (every 6 will be followed by at
least one 7). Return 0 for no numbers.'''

def sum67(nums):

    s = 0

    if len(nums) < 1:
        return s

    else:
        add = True
        for ele in nums:
            if ele == 6:
                add = False
            if add:
                s += ele
            if ele == 7:
                add = True
        return s

    # This is a working solution with while-loop
    #else:
    #    res = nums
    #    while 6 in res:
    #        del res[res.index(6):res.index(7, res.index(6))+1]
    #    s = sum(res)

    return s
#
#
#
# has22#
'''Given an array of ints,
return True if the array contains a 2 next to a 2 somewhere.'''

def has22(nums):
    is22 = False
    for i, val in enumerate(nums):
        if val == 2 and i != len(nums) - 1:
            if nums[i+1] == 2:
                is22 = True
        else:
            continue

    return is22
