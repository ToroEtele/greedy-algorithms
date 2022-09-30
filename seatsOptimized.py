#There is a row of empty (.) and filled (x) setats.
#Find the minimum number od moves required to make the people sit together

A = [".", "x", ".", ".", "x", ".", ".", "x", "x", "."]

MOD = 10000003

#all the indexes of Xs
crosses = [i for i, c in enumerate(A) if c == "x"]  #[1, 4, 7, 8]
#number of moves required asuming start position of the segment is 0
crosses = [(cross - i) for i, cross in enumerate(crosses)] #[1, 3, 5, 5]

n = len(A)
ans = float('inf')

if n == 0: 
  ans = 0
else:
  segment_start = crosses[n // 2]
  total = 0
  for cross in crosses:
    total += abs(cross - segment_start)
    total %= MOD
  ans = min(ans, total % MOD)

print(ans)