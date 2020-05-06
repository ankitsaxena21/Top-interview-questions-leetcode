class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store=[]                          
        for i in nums1:                   
            if i in nums2:                
                nums2.remove(i)           
                store.append(i)           
        return store 
