class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        # pointer = 1
        # count = 0

        # for num in range(1,len(nums)):
            
        #     if nums[num] == nums[num-1]:
        #         count +=1
                    
        #     else:
        #         count = 0
                    
        #     if count <= 2:
        #         nums[pointer] = nums[num]
        #         pointer +=1

        # pointer = 2  #  pointer starting from index 2
        # for num in range(2, len(nums)):
        #     if nums[num] != nums[num - 2]:  # If current element is different from two positions before slow
        #         nums[pointer] = nums[num]
        #         pointer += 1


        # j = 1
        # for i in range(1, len(nums)):
        #     if j == 1 or nums[i] != nums[j - 2]:
        #         nums[j] = nums[i]
        #         j += 1
        # return j

        pointer = 1
        count = 1

        for num in range(1,len(nums)):
            
            if nums[num] == nums[num - 1]:
                count +=1
                    
            else:
                count = 1
                    
            if count <= 2:
                nums[pointer] = nums[num]
                pointer +=1
        return pointer