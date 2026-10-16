class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map ={}

        for i in range(len(s)):
            map[s[i]] = map.get(s[i],0)+1
        for j in range(len(t)):
            map[t[j]] = map.get(t[j],0)-1
        
        for count in map.values():
            if(count != 0):
                return False
        return True