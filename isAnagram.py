# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
        
def isAnagram(s: str, t: str) -> bool:
    cFlag = False

    if len(s) != len(t):
        return cFlag

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

         
def testCase1():
    s = "racecar"
    t = "carrace"
    print(isAnagram(s, t))

    return

 
def testCase2():
    s = "jar"
    t = "jam"
    print(isAnagram(s, t))

    return

testCase1()
testCase2()
