#Given array of integers of legth N
#Majority element occurs with > N/2 frequency
#Find the majority element

from collections import Counter

class NaiveSolution:
  def majorityElement(self, A):
    return Counter(A).most_common(1)[0][0]

class SneakySolution:
  def majorityElement(self,A):
    n = len(A)
    ans = 0
    
    for b in range(32):
      ones = 0
      for num in A:
        if (1 << b) & num: 
          ones += 1
      if ones > n // 2: 
        ans += ( 1 << b)
    
    return ans