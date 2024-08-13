# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

def twoSum(nums: list[int], target: int) -> list[int]:
    
    for i in range(len(nums) - 1):
        j = len(nums) - 1
        while (j > i):
            if nums[i] + nums[j] == target:
                return [i, j]
            j -= 1

         
def testCase1():
    nums = [3,4,5,6]
    target = 7
    print(twoSum(nums, target))

    return

 
def testCase2():
    nums = [4,5,6]
    target = 10
    print(twoSum(nums, target))

    return

testCase1()
testCase2()
