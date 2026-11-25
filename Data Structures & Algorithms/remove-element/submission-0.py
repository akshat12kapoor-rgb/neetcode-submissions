class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #initalise k
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)

        #for each value in nums:
           #check if that value = val
                #if no, increase k and continue
                #if yes, pop the value at that index
        
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for the next non-val position
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k
