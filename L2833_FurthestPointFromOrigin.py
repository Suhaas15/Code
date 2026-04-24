class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # seen={}
        # for char in moves:
        #     seen[char] = seen.get(char,0) + 1

        # pos=0
        # for i in range(len(moves)):
        #     if moves[i]=="L":
        #         pos-=1
        #     elif moves[i]=="R":
        #         pos+=1
        #     else:
        #         if seen.get('L',0)>=seen.get('R',0):
        #             pos-=1
        #         else:
        #             pos+=1
        
        # return abs(pos)

        L = moves.count('L')
        R = moves.count('R')

        pos = 0
        for c in moves:
            if c == 'L':
                pos -= 1
            elif c == 'R':
                pos += 1
            else:
                pos += 1 if R > L else -1

        return abs(pos)

            
