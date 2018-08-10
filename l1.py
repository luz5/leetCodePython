class Solution:
    def twoSum(self, nums, target):  # leetcode runtime: 40ms
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = {}
        for i, n in enumerate(nums):
            if target - n in ans:
                return [ans[target-n], i]
            ans[n] = i

    def twoSum2(self, nums, target):  # leetcode runtime: 40ms
        look_for = {}
        for n, x in enumerate(nums):
            try:
                return look_for[x] + 1, n + 1
            except KeyError:
                look_for.setdefault(target - x, n)

    def twoSum3(self, nums, target):  # In dev
        ans = [0] * (max(max(nums), target) ** 2)
        print(len(ans))
        for i, n in enumerate(nums):
            look_for = target - n
            if ans[look_for] != 0:
                return [ans[look_for] - 1, i]
            else:
                ans[n] = i + 1


a = Solution()
print(a.twoSum3([-1, -2, -3, -4, -5], -8))

# 66898183
# 2341



