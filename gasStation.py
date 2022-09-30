# There are N gas stations along a circular route
# Each has A[i] amount of gas.
# To travel from station i -> i+1 there is a B[i] cost
# Find the earliest station from where you can travel around the entire circuit


class Solution:
  def canCompleteCircuit(self,A,B):
    n = len(A)

    curr = start = 0
    for i, (g, c) in enumerate(zip(A*2, B*2)):
      if i == start + n:    #ha körbe ért vége
        return start
      
      curr += g-c           #kiszámolom mennyi üzemanyag maradt

      if curr < 0:          #ha 0-nál kevesebb akkor a start lép tovább
        start = i + 1
        curr = 0            #az üzemanyag nullázódik
    return -1