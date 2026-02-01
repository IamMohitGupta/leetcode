class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        first = strs[0]
        pref=""
        for i in range(len(first)):
            for j in range(1,len(strs)):
                if i>=len(strs[j]) or first[i]!=strs[j][i]:
                    return pref
            pref+=first[i]
        
        return pref
