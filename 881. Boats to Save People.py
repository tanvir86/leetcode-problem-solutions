class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        
        res, left, right = 0, 0, len(people)-1
        
        while  left <= right:
            # if left == right:
            #     left += 1
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
                
            res += 1
        return res
