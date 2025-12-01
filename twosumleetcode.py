class Solution:
    def twoSum(self, nums, target):
        seen = {}   # value -> index

        for i, value in enumerate(nums):
            diff = target - value

            if diff in seen:
                return [seen[diff], i]

            seen[value] = i
