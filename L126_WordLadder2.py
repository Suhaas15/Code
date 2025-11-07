class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words,mp,ans=set(wordList),defaultdict(list),[]
        def bfs(words):
            letters=[chr(97+x) for x in range(26)]
            ws,q,next_lev=len(beginWord),deque([beginWord]),set()
            while q:
                size=len(q)
                for _ in range(size):
                    w=q.popleft()
                    for i in range(ws):
                        pre,suf=w[:i],w[i+1:]
                        for l in letters:
                            nw=pre+l+suf
                            if nw in words:
                                mp[nw].append(w)
                                next_lev.add(nw)
                q.extend(next_lev)
                words-=next_lev
                next_lev.clear()
        bfs(words)
        def dfs(w,arr):
            if w==beginWord:
                ans.append(list(arr))
                return
            for nw in mp[w]:
                arr.appendleft(nw)
                dfs(nw,arr)
                arr.popleft()
        if endWord in mp:
            dfs(endWord,deque([endWord]))
        return ans
