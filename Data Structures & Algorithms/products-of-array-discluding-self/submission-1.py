class Solution:
    def productExceptSelf(nums):
        n = len(nums)
        output = [1] * n
    
        # Step 1: Prefix products
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
    
        # Step 2: Suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
    
        return output
    