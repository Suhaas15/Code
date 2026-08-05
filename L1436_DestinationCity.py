class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        freq={}

        for path in paths:
            freq[path[0]] = freq.get(path[0],0)+1
            freq[path[1]] = freq.get(path[1],0)-1

        for key, val in freq.items():
            if val==-1:
                return key
