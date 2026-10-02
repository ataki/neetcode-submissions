class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = dict([(el, i) for i, el in enumerate(nums)])
        for i in range(len(nums)):
            if (target - nums[i]) in ref and ref[target - nums[i]] != i:
                return sorted([i, ref[target -nums[i]]])
        raise Exception("Answer should exist")
        