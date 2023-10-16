class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=j=0
        if s == "":
            return True
        elif t =="":
            return False

        if len(t)>len(s):
            t,s = s,t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j +=1
                i +=1
            else:
                i +=1
        else:
            return j == len(t)
        