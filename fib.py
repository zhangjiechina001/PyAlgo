from numpy import ndarray
import numpy as np

class Fib:

    def fib(self,n):
        memo = {}
        return self._fib_helper3(n, memo)

    def fib_helper1(self,n,memo):
        if(n in memo):
            return memo[n]

        if(n==1 or n==2):
            return  1

        memo[n]=self.fib_helper1(n-1,memo)+self.fib_helper1(n-2,memo)
        return memo[n]

    def _fib_helper2(self,n,memo):
        if(n==1 or n==2):
            return  1

        dp=[None]*(n+1)
        dp[0:3]=[0,1,1]
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return  dp[n]

    def _fib_helper3(self,n,memo):
        if(n==1 or n==2):
            return  1

        dp=[None]*(n+1)
        dp[0:3]=[0,1,1]
        curr=1
        prev=1
        for i in range(3,n+1):
            sum=curr+prev
            prev=curr
            curr=sum

        return  curr



if(__name__=='__main__'):
    fib=Fib()
    print(fib.fib(10))