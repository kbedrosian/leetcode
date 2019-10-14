import functools
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = collections.defaultdict(list)
        for s in strs:
            counts = collections.defaultdict(int)
            for c in s:
                counts[c] += 1
            result[tuple(sorted(counts.items(), key=lambda (l, c): l))].append(s)
        return result.values()
