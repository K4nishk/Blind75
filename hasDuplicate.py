# class Solution:
# def hasDuplicate(self, nums: List[int]) -> bool:
def hasDuplicate(nums: list[int]) -> bool:
    num_set = set(nums)

    if len(num_set) != len(nums):
        return True
    else:
        return False
         
def testCase1():
    nums = [1, 2, 3, 3]
    print(hasDuplicate(nums))

    return

 
def testCase2():
    nums = [1, 2, 3, 4]
    print(hasDuplicate(nums))

    return

testCase1()
testCase2()
