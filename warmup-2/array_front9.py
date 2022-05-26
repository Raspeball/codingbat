def array_front9(nums):
    if len(nums) < 4:
        front = nums
    else:
        front = nums[0:4]
    
    return (9 in front)