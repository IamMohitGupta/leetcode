class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        open = ['(','{','[']
        for i in s:
            if len(l)==0:
                l.append(i)
            else:
                if i in open:
                    l.append(i)
                else:
                    if i ==')' and l[-1] == '(':
                        l.pop()
                    elif i =='}' and l[-1] == '{':
                        l.pop()
                    elif i ==']' and l[-1] == '[':
                        l.pop()
                    else:
                        return False
        if len(l) == 0:
            return True
        return False 

"""

top and pop approach

"""
