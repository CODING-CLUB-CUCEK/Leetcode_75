class Solution:
    def reverseVowels(self, s: str) -> str:
        vow='aeiouAEIOU'
        a=list(s)
        b=[]
        out=''
        for i in range(len(a)):
            if a[i] in vow:
                b.append(a[i])
                a[i]=0
        b.reverse()
        count=0
        for i in range(len(a)):
            if a[i] == 0:
                out+=b[count]
                count+=1
            else:
                out+=a[i]
        return out