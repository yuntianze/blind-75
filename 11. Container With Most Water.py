"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the i^th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers at the start and end of the array
        left, right = 0, len(height) - 1
        max_area = 0
        # Loop until the two pointers meet
        while left < right:
            # Calculate the area formed by the lines at left and right
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            # Update max_area if the current area is larger
            max_area = max(max_area, area)
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
    print(solution.maxArea([1,1]))
    print(solution.maxArea([1,2,1]))
    print(solution.maxArea([1,2,4,3]))
    print(solution.maxArea([1,2,4,3,5]))
