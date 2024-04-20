def find_max(lst):
  if not lst:
    return none
  elif len(lst) == 1:
    return lst[0]
  else:
    max_of_rest = find_max(lst[1:])
    return lst[0] if lst[0] > max_of_rest else max_of_rest