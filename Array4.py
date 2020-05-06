class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        items = set(nums)
        return not (len(items) == len(nums))
