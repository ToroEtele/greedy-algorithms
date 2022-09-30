#N kids stand in the line, each having an integer rating. We distribute candies following:
  # each kid gets at least 1 candy
  # kids with higher ratings than their neighbours get more candy
#Find the minimum candies required

A = [1, 3, 7, 6, 5, 5, 2]

n = len(A)
data = sorted((x, i) for i, x in enumerate(A)) # we are going to sort the kids by their rating

candies = [1] * n   

for _, i in data:
  if i > 0 and A[i] > A[i-1]:     # if smaller than previous and not first element
    candies[i] = max(candies[i], candies[i-1] + 1)  # here is useless the max()
  if i < n - 1 and A[i] > A[i+1]: # if greater tham next and not the last element
    candies[i] = max(candies[i], candies[i+1] + 1) # if candies[i-1] > candies[i] and candies[i+1]. And candies[i] < candies[i+1]

total = sum(candies)