#參考claude的答案
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}  # 建立一個字典來儲存已經遍歷過的數字及其索引
    
        for i, num in enumerate(nums):
            complement = target - num  # 計算與當前數字匹配的另一個數字
            
            # 檢查這個匹配的數字是否已經在字典中
            if complement in num_dict:
                return [num_dict[complement], i]
            
            # 將當前數字和索引加入字典
            num_dict[num] = i

        