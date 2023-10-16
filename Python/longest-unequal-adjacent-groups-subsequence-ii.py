# Time:  O(n^2)
# Space: O(n)

import itertools


# dp, backtracing
class Solution(object):
    def getWordsInLongestSubsequence(self, n, words, groups):
        """
        :type n: int
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        def check(i, j):
            return (groups[i] != groups[j] and
                    len(words[i]) == len(words[j]) and
                    sum(a != b for a, b in itertools.izip(words[i], words[j])) == 1)

        dp = [[1, -1] for _ in xrange(n)]
        for i in reversed(xrange(n)):
            for j in xrange(i+1, n):
                if check(j, i):
                    dp[i] = max(dp[i], [dp[j][0]+1, j])
        result = []
        i = max(xrange(n), key=lambda x: dp[x])
        while i != -1:
            result.append(words[i])
            i = dp[i][1]
        return result


# Time:  O(n^2)
# Space: O(n)
import itertools


# dp, backtracing
class Solution2(object):
    def getWordsInLongestSubsequence(self, n, words, groups):
        """
        :type n: int
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        def check(i, j):
            return (groups[i] != groups[j] and
                    len(words[i]) == len(words[j]) and
                    sum(a != b for a, b in itertools.izip(words[i], words[j])) == 1)

        mx = [0, -1]
        dp = [[1, -1] for _ in xrange(n)]
        for i in xrange(n):
            for j in xrange(i):
                if check(j, i):
                    dp[i] = max(dp[i], [dp[j][0]+1, j])
            mx = max(mx, [dp[i][0], i])
        result = []
        i = max(xrange(n), key=lambda x: dp[x])
        while i != -1:
            result.append(words[i])
            i = dp[i][1]
        result.reverse()
        return result
