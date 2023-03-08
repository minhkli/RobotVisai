a = [1,2,3,4,5,6,7,8,9,10,11]

def is_sochan(x):
  if (x%2):
    return 1
  else:
    return 0

out = filter(is_sochan,a)
list(out)