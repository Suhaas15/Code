class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s="".join(chunks)

        words=[]
        cur=[]

        for i, ch in enumerate(s):
            if ch.islower():
                cur.append(ch)
            
            elif (ch == '-' and i > 0 and i < len(s) - 1 and s[i - 1].islower() and s[i + 1].islower()):
                cur.append(ch)
            
            else:
                if cur:
                    words.append("".join(cur))
                    cur=[]
            
        if cur:
            words.append("".join(cur))
        
        freq={}
        for w in words:
            freq[w] = freq.get(w,0) + 1
        
        return [freq.get(q,0) for q in queries]
