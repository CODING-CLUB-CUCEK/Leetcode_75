class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lenx,leny=len(word1),len(word2)
        i=0
        c=''
        while i<min(lenx,leny):
            c+=word1[i]
            c+=word2[i]
            i+=1
        else:
            if lenx>leny:
                c+=word1[i:]
            else:
                c+=word2[i:]
        return c