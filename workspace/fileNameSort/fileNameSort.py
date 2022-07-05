import os,shutil

#  找到字符串中连续相同的部分
#  minLen:默认有三个相同的字符,即表明是字符串中有相同的部分
def stringFindSamePart(strA,strB,minLen = 3):
    def findsame(strA,strB,sameLen=3):  # 找到长度为sameLen的相同连续字符串
        haveSame = False
        for s1_index in range(len(strA)-sameLen):
            s1_part = str()     # 拼接连续的sameLen个字符,组成字符串
            for temp_index in range(sameLen):
                s1_part += strA[s1_index+temp_index]
            if s1_part in strB:     # 判断拼接的字符串是否在另一个字符串中
                haveSame = True
                break
        if haveSame == True:
            return s1_part
        return False

    # 匹配到尽量多的相同字符串
    samelen = minLen     # 最少要有3个连续的字符串相同
    retSameStr = str()
    while True:
        sameStr = findsame(strA=strA,strB=strB,sameLen=samelen)
        if sameStr != False:    # 如果匹配到了
            retSameStr = sameStr # 记录匹配到的相同的字符串
            samelen += 1
        else:
            break
    return retSameStr

    

if __name__ == "__main__":
    str01 = "ccc"
    str02 = "aaaCPDE-006HEVC[cmfpans]"
    result = stringFindSamePart(strA=str01,strB=str02)
    print(result)