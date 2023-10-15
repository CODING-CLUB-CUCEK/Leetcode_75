class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge=""
        n=len(word1)
        m=len(word2)
        a = min(n,m)
        count=0
        for i in range(0,a):
            merge+=word1[i]+word2[i]
            count=i
        if(len(word1)>len(word2)):
            merge+=word1[count+1:n]
        else:
            merge+=word2[count+1:m]
        return merge