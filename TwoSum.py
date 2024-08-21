class TwoSum(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if index1 != index2 and value1+value2==target:
                    return [index1,index2]
