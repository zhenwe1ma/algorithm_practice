from typing import List


class Solution:
    """
    LeetCode 912. Sort an Array

    Practice target:
        Implement the sorting logic with selection sort.

    Input:
        nums: An integer array.

    Output:
        Return the array sorted in ascending order.
    """

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     def selectSmallestElement(nums: List[int]) -> int:
    #         item = nums[0]
    #         index = 0
    #         for i in range(len(nums)):
    #             if nums[i] < item:
    #                 item = nums[i]
    #                 index = i
    #         return index

    #     newArray = []
    #     for i in range(len(nums)):
    #         i = selectSmallestElement(nums)
    #         newArray.append(nums[i])
    #         nums.pop(i)
    #     return newArray

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     for i in range(n):
    #         min_index = i
    #         for j in range(i + 1, n):
    #             if nums[j] < nums[min_index]:
    #                 min_index = j
    #         if min_index != i:
    #             nums[i], nums[min_index] = nums[min_index], nums[i]
    #     return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if nums[min_index] > nums[j]:
                    min_index = j
            if min_index != i:
                nums[min_index], nums[i] = nums[i], nums[min_index]
        return nums
