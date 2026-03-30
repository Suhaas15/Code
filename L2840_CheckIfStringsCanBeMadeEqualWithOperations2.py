class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_balance = [0] * 26
        odd_balance = [0] * 26

        for i in range(len(s1)):
            if i%2==0:
                even_balance[ord(s1[i]) - ord('a')] +=1
                even_balance[ord(s2[i]) - ord('a')] -=1
            
            else:
                odd_balance[ord(s1[i]) - ord('a')] +=1
                odd_balance[ord(s2[i]) - ord('a')] -=1
            
        return all(count==0 for count in even_balance) and all(count==0 for count in odd_balance)
