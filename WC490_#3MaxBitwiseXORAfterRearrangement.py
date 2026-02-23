class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        zeros=t.count("0")
        ones=len(t)-zeros

        res=[]
        for char in s:
            if (char=="1" and zeros) or (char=="0" and ones):
                res.append("1")
                zeros-=(char=="1")
                ones-=(char=="0")
            
            else:
                res.append("0")
                ones-=(char=="1")
                zeros-=(char=="0")
            
        return "".join(res)
