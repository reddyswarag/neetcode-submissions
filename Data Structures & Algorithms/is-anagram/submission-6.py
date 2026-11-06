class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        countt = {}
        if len(s) != len(t):
            return False
        for i in range(0, len(s)):
            if s[i] not in counts.keys():
                counts[s[i]] = 1
            else:
                counts[s[i]] += 1
        for i in range(0, len(t)):
            if t[i] not in countt.keys():
                countt[t[i]] = 1
            else:
                countt[t[i]] += 1
        for key in counts.keys():
            if key not in countt.keys():
                return False
            elif counts[key] != countt[key]:
                return False

            
        return True


            
        
        
        