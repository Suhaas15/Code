class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        # freq={}
        # for bulb in bulbs:
        #     freq[bulb] = 1 + freq.get(bulb,0)
        
        # ans=[]
        # for i,num in freq.items():
        #     if num%2!=0:
        #         ans.append(i)
        # ans.sort()
        # return ans

        on=set()

        for bulb in bulbs:
            if bulb in on:
                on.remove(bulb)
            else:
                on.add(bulb)
        
        return sorted(on)
