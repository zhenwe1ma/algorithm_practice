from typing import List


class Solution:
    """
    LeetCode 704. Binary Search

    Input:
        nums: A sorted integer array in ascending order.
        target: The integer to search for.

    Output:
        Return the index of target if it exists in nums.
        Return -1 otherwise.
    """

    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]
            if guess < target:
                low = mid + 1
            elif guess > target:
                high = mid - 1
            else:
                return mid
        return -1
