import random
import copy

# def rand_status(src):
#   flag = True
#   status = copy.deepcopy(src)
#   while flag:
#     random.shuffle(status)
#     count = 0
#     for i in range(len(status)):
#       current = status[i]
#       if current == 0:
#         continue
#       for j in range(i):
#         if status[j] > current:
#           count += 1
#     if count % 2 == 0:
#       flag = False
#   return status

def rand_status(src, step):
  cstep = 0
  zero = -1
  direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]
  for i in range(len(src)):
    if src[i] == 0:
      zero = i
  while cstep < step:
    r = random.randint(0, 3)
    d = direction[r]
    idx = zero + d[0] * 3 + d[1]
    if idx >= 0 and idx <= 8:
      src[idx], src[zero] = src[zero], src[idx]
      zero = idx
      cstep += 1
  return src

def generate_subsequent_node(status):
  direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]
  zero = -1
  result = []
  for i in range(len(status)):
    if status[i] == 0:
      zero = i
  for d in direction:
    idx = zero + d[0] * 3 + d[1]
    zero_row = zero // 3
    zero_col = zero  % 3
    if zero_row + d[0] < 0 or zero_row + d[0] >= 3:
      continue
    if zero_col + d[1] < 0 or zero_col + d[0] >= 3:
      continue
    if idx >= 0 and idx <= 8:
      new_status = copy.deepcopy(status)
      new_status[idx], new_status[zero] = new_status[zero], new_status[idx]
      result.append(new_status)
  return result

