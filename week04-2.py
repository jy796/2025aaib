# week04-2.py �O���Ѫ� Leetcode �D���D  easy �D(�G�X�@)
# Leetcode 2529. Maximum count of Positive Integer
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0 # �j��e�� �ǳƦn,����0
        for i in range(len(nums)): # �j����A��s��
            if nums[i] > 0:pos += 1
            if nums[i] < 0:neg += 1
        # �j��᭱�A�⵪�׮��ӥ�
        return max(pos, neg)
