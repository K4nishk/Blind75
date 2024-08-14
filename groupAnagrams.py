# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

      
def isAnagram(s: str, t: str) -> bool:
    cFlag = False

    if len(s) != len(t):
        return cFlag

    if len(s) == 0:
        return True
    
    s_dict = {}
    for c in s:
        if c not in s_dict:
            s_dict[c] = 1
        else:
            s_dict[c] += 1

    t_dict = {}
    for c in t:
        if c not in t_dict:
            t_dict[c] = 1
        else:
            t_dict[c] += 1
    
    for c in s_dict:
        if c not in t_dict:
            cFlag = False
            break
        else:
            if s_dict[c] != t_dict[c]:
                cFlag = False
                break
            else:
                cFlag = True

    return cFlag

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = []
    res = []

    for i in range(len(strs)):
        if strs[i] == "":
            res

        if strs[i] not in res:
            res.append(strs[i])
            
            anagrams = []
            anagrams.append(strs[i])

            j = len(strs) - 1
            while (j > i):
                if isAnagram(strs[i], strs[j]):
                    anagrams.append(strs[j])
                    res.append(strs[j])
                
                j-=1

            result.append(anagrams)

    return result


         
def testCase1():
    strs = ["act","pots","tops","cat","stop","hat"]
    print(groupAnagrams(strs))

    return

 
def testCase2():
    strs = ["x"]
    print(groupAnagrams(strs))

    return

def testCase3():
    strs = [""]
    print(groupAnagrams(strs))

    return

def testCase4():
    strs=["",""]
    # print(groupAnagrams(strs))
    print(isAnagram(strs[0], strs[1]))

    return

testCase1()
testCase2()
testCase3()
testCase4()