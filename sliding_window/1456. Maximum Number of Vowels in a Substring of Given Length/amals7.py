class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel =set("aeiou")
        def count(s1):
          c=0
          for char in s1:
            if char in vowel:
              c +=1
          return c

        maxlen =current = count(s[:k])
        j=0
        # vowels =set("aeiou")
        for i in range(k,len(s)):
          if s[j] in vowel and s[i] not in vowel:
            current -=1
          elif s[j] not in vowel and s[i] in vowel:
            current  +=1
          maxlen = max(current,maxlen)
          j +=1
          

        return maxlen

