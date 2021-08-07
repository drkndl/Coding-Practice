class Solution:
    def reverse(self, x: int) -> int:
        negnum=False
        self.x=x
        rev=0
        if self.x*(-1)>0:
            negnum=True
        while(abs(self.x)>0):
            digit=int(abs(self.x)%10)
            rev=rev*10+digit
            self.x=abs(self.x)//10
        if negnum==True and -2**31 <= rev < 2**31:
             return -1*rev
        elif negnum==False and -2**31 <= rev < 2**31:
            return rev
        else:
            return 0
     
        
