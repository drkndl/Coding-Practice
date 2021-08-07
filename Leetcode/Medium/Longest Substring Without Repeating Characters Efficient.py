#Run time: 76ms (57.82%)
#Memory: 14MB (28.35%)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        self.s=s
        seen={}
        maxcount=0
        start=0
        for end in range(len(self.s)):
            if self.s[end] in seen:
                start=max(start,seen[self.s[end]]+1)
            seen[self.s[end]]=end
            maxcount=max(maxcount,end-start+1)
        return maxcount
              
