import itertools

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        soFar = 1
        pForward = []
        for n in nums:
            soFar *= n
            pForward.append(soFar)

        soFar = 1
        pBackward = []
        for n in reversed(nums):
            soFar *= n
            pBackward.append(soFar)
        pBackward.reverse()

        result = []
        for i in range(len(nums)):
            p = 1
            if i > 0:
                p *= pForward[i-1]
            if i < len(nums)-1:
                p *= pBackward[i+1]
            result.append(p)
        return result

