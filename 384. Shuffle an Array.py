class Solution:

    def __init__(self, nums: List[int]):
        self.change = nums[:]
        self.original = nums[:]

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        for i in range(len(self.change)):
            x = random.randint(i,len(self.change)-1)
            self.change[i], self.change[x] = self.change[x], self.change[i]
        return self.change

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
