from py_linq import Enumerable
def coinChanged(coins,amount):
    memo={}
    def dp(n):
        if(n in memo):
            return  memo[n]

        if(n==0):
            return 0
        if(n<0):
            return float('INF')
        #先获取所有有效的子项
        sub_items=Enumerable(coins).select(lambda x:dp(n-x)).where(lambda t:t!=-1 and t!=float('INF')).to_list()
        #在获取当前最优结果
        memo[n]=sub_items.min()+1 if sub_items.any() else float('INF')
        return memo[n]

    return  dp(amount)

coins=[1,2,3,5]
result=coinChanged(coins,201)
print(result)



