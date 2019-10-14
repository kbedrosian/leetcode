class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        offset = 0
        while len(nums) > 1:
            midIdx = len(nums) // 2
            if nums[midIdx] == target:
                return offset + midIdx

            # The target is in the bottom half if:
            #   The pivot is in the bottom half and the target *is* there, or
            #   the pivot is in the top half, and the target is *not* there
            if ( nums[0] <= nums[midIdx] and nums[0] <= target < nums[midIdx] ) or \
               ( nums[midIdx] <= nums[-1] and not ( nums[midIdx] < target <= nums[-1] ) ):
                nums = nums[:midIdx]
            else:
                nums = nums[midIdx+1:]
                offset += midIdx+1
        if not nums:
            return -1
        else:
            return offset if nums[0] == target else -1
