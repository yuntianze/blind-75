"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store number and its index
        num_to_index = {}
        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            # If complement exists in the dictionary, return the indices
            if complement in num_to_index:
                return [num_to_index[complement], i]
            # Otherwise, store the number and its index in the dictionary
            num_to_index[num] = i
        # If no solution is found (should not happen as per problem statement)
        return []
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([3, 3], 6))
    print(solution.twoSum([-1, -2, -3, -4, -5], -8))
    