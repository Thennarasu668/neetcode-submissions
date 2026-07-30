class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        # Shrink the window until it contains exactly k elements
        while right - left >= k:
            # Compare the distance of the left-most element and the right-most element from x
            # If the left element is farther, increment the left pointer
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            # If the right element is farther or distances are equal (tie-breaker prefers smaller element), 
            # decrement the right pointer
            else:
                right -= 1
        
        # Return the final window of k elements
        return arr[left : right + 1]



