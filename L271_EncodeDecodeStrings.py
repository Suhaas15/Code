from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        pieces=[]
        for w in strs:
            pieces.append(f"{len(w)}#{w}")
        return "".join(pieces)
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        n=len(s)

        while i<n:
            j=s.find("#",i)
            length=int(s[i:j])

            i=j+1
            word=s[i: i+length]
            res.append(word)

            i+=length
        return res
