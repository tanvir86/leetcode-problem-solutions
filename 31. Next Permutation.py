class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 1,2,3,4 -> 1,2,4,3 -> 1,3,2,4 -> 1,3,4 ,2 -> ....-> 4,3,2,1 -> reverse

        # if left < right  -> find immidiate greater number of left -> swap it with left -> reverse everything after left index
        
        def swap(x,y):
            temp = nums[x]
            nums[x] = nums[y]
            nums[y] = temp
        
        i = len(nums)-1
        
        while i >= 1:
            if nums[i-1] < nums[i]:
                r = len(nums)-1
                
                while nums[r] <= nums[i-1]:
                    r -= 1

                swap(r, i-1)
                
                # reverse from ith index to last
                # nums[i:] = nums[i:][::-1]
                
                l,r = i, len(nums)-1

                while l < r:
                    swap(l,r)
                    
                    l += 1
                    r -= 1
                    
                return nums
            
            i -= 1
        
        nums.reverse()
