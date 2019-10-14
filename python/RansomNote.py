import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = collections.defaultdict(int)
        for l in magazine:
            counts[l] += 1

        for l in ransomNote:
            if counts[l] <= 0:
                return False
            counts[l] -= 1
        return True
