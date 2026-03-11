class Solution:
    def decodeString(self, s: str) -> str:
        l = []
        result=""
        for i in s:
            if i!=']':
                l.append(i)
            else:
                ds=""
                while l[-1]!='[':
                    ds = l.pop()+ds
                l.pop()

                num=""
                while l and l[-1].isdigit():
                    num=l.pop()+num
                k = int(num)

                l.append(ds*k)
        return "".join(l)
