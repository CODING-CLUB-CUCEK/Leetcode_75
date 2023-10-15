class Solution:
    


    def mergeAlternately(self, word1: str, word2: str) -> str:
        def merge(word1,word2):
            merged_word = str()
            for i in range(len(word1)):
                merged_word+=word1[i]
                merged_word+=word2[i]
            return(merged_word)
        
        n1 = len(word1)
        n2 = len(word2)

        if n1 == n2:
            return merge(word1,word2)
        elif n1 < n2:
            end = word2[n1:]
            word2 = word2[:n1]
            return merge(word1,word2)+end
        else:
            end = word1[n2:]
            word1 = word1[:n2]
            return merge(word1,word2)+end

        