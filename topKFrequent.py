# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
def topKFrequent(nums, k):
    result = []

    num_dict = {}
    for val in nums:
        if val not in num_dict:
            num_dict[val] = 1
        else:
            num_dict[val] += 1

    max_occurence = 1
    for i in num_dict:
        if num_dict[i] > max_occurence:
            max_occurence = num_dict[i]
    
    while (max_occurence > 0):
        for i in num_dict:
            if num_dict[i] == max_occurence:
                result.append(i)
                
                if len(result) == k:
                    return result
    
        max_occurence -= 1

    return result

         
def testCase1():
    nums = [1,2,2,3,3,3]
    k = 2
    print(topKFrequent(nums, k))

    return

 
def testCase2():
    nums = [7,7]
    k = 1
    print(topKFrequent(nums, k))

    return

def testCase3():
    nums=[4,1,-1,2,-1,2,3]
    k = 2
    print(topKFrequent(nums, k))

    return


testCase1()
print("======")
testCase2()
print("======")
testCase3()

