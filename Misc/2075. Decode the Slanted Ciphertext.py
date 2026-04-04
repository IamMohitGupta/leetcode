class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        x = len(encodedText)
        cols = x//rows
        result = ""
        for i in range(cols):
            result+=encodedText[i]
            j = i+cols+1
            while j<x:
                result+=encodedText[j]
                j+=cols+1
        return result.rstrip(' ')
