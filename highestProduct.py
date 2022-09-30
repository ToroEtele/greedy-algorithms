class Solution:
  # A is an array of integers
  # Return the highest product of: 3 + numbers or 2 - number and one + number
  def maxp3(self, A):
    A = sorted(A)

    hi3 = A[-1] * A[-2] * A[-3]
    lo2hi1 = A[0] * A[1] * A[-1]

    return max(hi3, lo2hi1)

  print(maxp3([1,-2,-3,5,6]))
# obj = Solution()