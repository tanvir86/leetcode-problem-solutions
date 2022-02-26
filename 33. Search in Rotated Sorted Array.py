class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = int((left + right)/2)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[left]: #left side is sorted
                if nums[mid] > target and target >= nums[left]:
                    right = mid -1
                else:
                    left = mid + 1
            else: # right side is sorted
                if left == mid: # handle when left == mid. we will not see right== mid as int cast resulting in floor
                    left = mid + 1
                elif nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
                        
        return -1                
            