class Solution(object):
    def reverse(self, x):
        y=x
        x=int(str(abs(x))[::-1])
        if (abs(x) > (2 ** 31 - 1)):
            x=0
        return -x if(y<0) else x
print(2 ** 31 - 1)
val=Solution().reverse(1534236469)
print(val)
