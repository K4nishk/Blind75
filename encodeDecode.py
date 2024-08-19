# class Solution:

#     def encode(self, strs: List[str]) -> str:

#     def decode(self, s: str) -> List[str]:

def encode(strs: list[str]) -> str:
    encoded = ''

    if len(strs) == 0:
        return encoded
    
    if len(strs) == 1:
        if strs[0] == '':
            return ',-,'

    if strs[0] == '':
        encoded += ',-,'

    for i in range(len(strs)):
        if i == len(strs) - 1:
            encoded += strs[i]        
        else:
            encoded += strs[i] + ',-,'

    return encoded

def decode(s: str) -> list[str]:
    if len(s) == 0:
        return []
    else:
        if s == ',-,':
            return [""]
        
        result = s.split(',-,')

        if result[0] == '':
            result.remove('')
            
        return result


def testCase1():
    strs = ["neet","code","love","you"]
    s = encode(strs)
    print(decode(s))

    return

 
def testCase2():
    strs = ["we","say",":","yes"]
    s = encode(strs)
    print(decode(s))

    return

def testCase3():
    strs = []
    s = encode(strs)
    print(decode(s))

    return

def testCase4():
    strs = [""]
    s = encode(strs)
    print(decode(s))

    return

def testCase5():
    strs = ["The quick brown fox","jumps over the","lazy dog","1234567890","abcdefghijklmnopqrstuvwxyz"]
    s = encode(strs)
    print(decode(s))

    return

def testCase6():
    strs = ["1,23","45,6","7,8,9"]
    s = encode(strs)
    print(decode(s))

    return

def testCase7():
    strs = ["VeryLongStringWithoutAnySpacesOrSpecialCharactersRepeatedManyTimesVeryLongStringWithoutAnySpacesOrSpecialCharactersRepeatedManyTimes"]
    s = encode(strs)
    print(decode(s))

    return


def testCase8():
    strs = ["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"]
    s = encode(strs)
    print(decode(s))

    return

testCase1()
print("======")
testCase2()
print("======")
testCase3()
print("======")
testCase4()
print("======")
testCase5()
print("======")
testCase6()
print("======")
testCase7()
print("======")
testCase8()