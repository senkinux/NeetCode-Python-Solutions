class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Time: O(n)
        Space: O(1), lookup table max alpha chars 26, so constant space.
        '''
        d = Counter(s1)
        l = 0
        for r in range(len(s2)):
            d[s2[r]] -= 1
            while d[s2[r]] < 0:
                d[s2[l]] += 1
                l += 1
            if r - l + 1 == len(s1):
                return True
        return False
