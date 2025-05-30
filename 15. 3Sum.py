"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to use two pointers technique
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n - 2):
            # Skip duplicate elements for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1
                elif total < 0:
                    # If the sum is too small, move the left pointer to increase the sum
                    left += 1
                else:
                    # If the sum is too large, move the right pointer to decrease the sum
                    right -= 1
        return result
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))
    print(solution.threeSum([0,1,1]))
    print(solution.threeSum([0,0,0]))
    print(solution.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
    