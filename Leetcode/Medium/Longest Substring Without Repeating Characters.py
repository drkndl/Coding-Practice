class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        self.s=s
        count=0
        maxcount=0
        letters=[]
        for i in range(len(self.s)):
            letters.append(self.s[i])
            if letters.count(self.s[i])==1:
                count=len(letters)
                if count>maxcount:
                    maxcount=count
            else:
                letters.clear()
                for item in range(i,-1,-1):
                    if self.s[item] not in letters:
                        letters.append(self.s[item])
                    else:
                        break
        return maxcount
