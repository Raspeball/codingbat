## https://codingbat.com/prob/p143951 ##
# lone_sum #

'''Given 3 int values, a b c, return their sum.
However, if one of the values is the same as another of the values,
it does not count towards the sum.'''

def lone_sum(a, b, c):

    nums = [a, b, c]
    unique = set(nums)

    if sum(nums) == sum(unique):
        res = sum(nums)

    else:
        res = sum([i for i in nums if nums.count(i) < 2])

    return res
