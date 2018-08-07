class Solution:
    def rob(self, nums):
        if len(nums) < 3:
            return max(nums, default=0)
        from_first = self.help_rob(nums, 0, 0)
        from_second = self.help_rob(nums, 1, 0)
        return max(from_first, from_second)

    def help_rob(self, nums, index, total_cash):
        if index >= len(nums):
            return total_cash

        total_cash = total_cash + nums[index]
        two_over = self.help_rob(nums, index + 2, total_cash)
        three_over = self.help_rob(nums, index + 3, total_cash)
        return max(two_over, three_over)
        
