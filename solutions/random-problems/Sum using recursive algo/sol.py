def recurrsive_sum(n):
  if n == 1:
    return 1
  else:
    return  n + recurrsive_sum(n-1)