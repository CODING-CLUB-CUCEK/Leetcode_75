class Solution:
    def compress(self, chars: List[str]) -> int:
        # s = set(chars)
        # dic = {}
        # for item in s:
        #     dic[item] = chars.count(item)
        # i =0
        # dic_key = list(dic.keys())
        # dic_key.sort()
        # i =0
        # n = len(chars)
        # for key in dic_key:
        #     chars.append(str(key))
        #     chars.append(str(dic[key]))
        # chars=chars[n:]
        # print(chars)
        # print(len(chars))
        # return len(chars)



        n = len(chars)
        if n < 2:
            return n
        
        i = j = 0
        while i < n:
            count = 1
            while i < n-1 and chars[i]==chars[i+1]:
                count +=1
                i +=1
            chars[j]=chars[i]
            j +=1
            if count>1:
                for val in str(count):
                    chars[j]=val
                    j +=1
            i +=1
        return j

       
         
        
            
            


