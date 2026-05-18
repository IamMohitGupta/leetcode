class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        memo = set()
        def dfs(index):
            nonlocal memo
            if index >= len(arr) or index < 0:
                return False
            if index in memo:
                return False
            if arr[index] == 0:
                return True
            memo.add(index)
            return dfs(index+arr[index]) or dfs(index-arr[index])

        return dfs(start)
