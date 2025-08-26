class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        n=len(val)
        items=[(val[i],wt[i],val[i]/wt[i]) for i in range(n)]
        items.sort(key=lambda x:x[2], reverse=True)
        total=0.0
        
        for value,weight,ratio in items:
            if capacity==0:
                break
            if weight<=capacity:    #take the whole item.
                total+=value
                capacity-=weight
            else:                   #take a fraction that will fit.
                fraction=capacity/weight
                total+=fraction*value
                capacity=0
        
        return total
                
