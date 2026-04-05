class Solution:
    def judgeCircle(self, moves: str) -> bool:
        values = {"L": -1, "R": 1, "U": 1, "D": -1}

        Vcheck, Hcheck=0,0

        for char in moves:
            if char == "U" or char=="D":
                Vcheck+=values[char]
            else:
                Hcheck+=values[char]
        
        return Vcheck==0 and Hcheck==0
