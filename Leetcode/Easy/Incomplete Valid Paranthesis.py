import numpy as np
class Solution:
    def isValid(self, s: str) -> bool:
        flag=True
        x=np.empty(0)
        count={'(':0, ')':0, '{':0, '}':0, '[':0, ']':0}
        brack={'(':[], ')':[], '{':[], '}':[], '[':[], ']':[]}
        for i in range(len(s)):
            count[s[i]]=count.get(s[i])+1
            brack[s[i]].append(i)
        if count['(']!=count[')'] or count['{']!=count['}'] or count['[']!=count[']']:
            flag=False
            return flag
        list1 = brack['(']
        list2 = brack[')']
        list3 = brack['{']
        list4 = brack['}']
        list5 = brack['[']
        list6 = brack[']']
        for i in len(list1):
            list1=brack[i]
            if abs(list1[i]-list2[i])%2 == 0:
                flag=False
                return flag
        for i in len(list3):
            list3=brack[i]
            if abs(list3[i]-list4[i])%2 == 0:
                flag=False
                return flag
        for i in len(list5):
            list1=brack[i]
            if abs(list5[i]-list6[i])%2 == 0:
                flag=False
                return flag
        return flag
