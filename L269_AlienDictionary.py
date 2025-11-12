from collections import defaultdict, deque

def alienDictionary(words):
    # Step 1: Initialize graph structures
    graph = defaultdict(set)
    indegree = {c: 0 for word in words for c in word}
    
    # Step 2: Build graph by comparing adjacent words
    for w1, w2 in zip(words, words[1:]):
        # Invalid prefix case
        if len(w1) > len(w2) and w1.startswith(w2):
            return ""
        
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    indegree[c2] += 1
                break  # stop after first difference
    
    # Step 3: Topological sort (Kahn’s algorithm)
    queue = deque([c for c in indegree if indegree[c] == 0])
    order = []
    
    while queue:
        c = queue.popleft()
        order.append(c)
        for nei in graph[c]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    
    # Step 4: Check for cycle
    if len(order) < len(indegree):
        return ""
    
    return "".join(order)
