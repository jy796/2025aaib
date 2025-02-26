# week02-3.py �g Leetcode
# LeetCode 1. Two Sun
# ���@��Ʀr nums �̭�[�����]�ۥ[,�Otarget
# nums[i] + nums[j] == target  ��� i �M j �ϱo�[�_�ӬO target
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        box = {} # ���@�ӽc�l,�̭���X�{�L���Ʀr
        # �ڭ̷Q�n��X target �o�ӥ[�`

        for i,num in enumerate(nums):
            other = target - num #�t�~�@�ӻݭn���� �i�H��X��taget
            if other in box: #�b�c�l��,���t�~�@�ӻݭn����
                return [ box[other], i ] # ��쵪��
            else: # �p�G�S���X�A���Ʀr���
                box[num] = i # �N��{�b���Ʀr num , ��� box �̭�
