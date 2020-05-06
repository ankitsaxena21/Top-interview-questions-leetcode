class Solution(object):
    def rotate(self, nums, k):
        if k > len(nums):
            k = k - len(nums)
        n_list = nums[-k:]
        for n in nums[:-k]:
            n_list.append(n)
        nums[:] = n_list
