class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==1:
            return 1

        if x==-1:
            if n%2==1:
                return -1
            else:
                return 1

        sign_power = 1 if n>=0 else -1
        res = 1
        n = abs(n)
        for i in range(n):
            res*=x
            if abs(res)>1000000000 or abs(res)<0.0000000001:
                break
        
        if sign_power==-1:
            res = 1/res

        return res
    