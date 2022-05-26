def array123(nums):
    seq = [1,2,3]
    
    if len(nums) < len(seq):
        return False
    else:
        for ind in range(len(nums) - 2):
            if nums[ind: ind + 3] == seq:
                return True
    
    return False