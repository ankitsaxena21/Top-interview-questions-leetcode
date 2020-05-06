class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        while True:
            try:
                if nums[j+1] == nums[j]:
                    nums.remove(nums[j])
                else:
                    j += 1
            except IndexError:
                return
