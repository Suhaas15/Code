class Solution:    
    def findPlatform(self,arr,dep):
        # arr.sort()                    #2 pointer approach
        # dep.sort()
        
        # i=j=0
        # max_count=count=0
        
        # while i<len(arr) and j<len(dep):
        #     if arr[i]<=dep[j]:
        #         count+=1
        #         i+=1
        #     else:
        #         count-=1
        #         j+=1
        #     max_count=max(max_count,count)
        
        # return max_count
        
        times=[]                            #using sweep line algorithm
        for i in range(len(arr)):
            times.append([dep[i],'d'])
            times.append([arr[i],'a'])
        
        times=sorted(times, key=lambda x:x[1])
        times=sorted(times, key=lambda x:x[0])
        
        count,max_count=0,0
        
        for i in range(2*len(arr)):
            if times[i][1]=='a':
                count+=1
                max_count=max(max_count,count)
            else:
                count-=1
        
        return max_count
