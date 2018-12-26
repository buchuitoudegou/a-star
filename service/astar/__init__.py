from .utils import rand_status, generate_subsequent_node
from .Graph import Graph
import copy

class Astar():
  def __init__(self, idx):
    self.open = []
    self.closed = []
    # self.initial_status = rand_status([1, 2, 3, 4, 5, 6, 7, 8, 0])
    # self.initial_status = [6, 1, 8, 7, 0, 2, 5, 3, 4]
    # self.initial_status = [1, 6, 2, 5, 3, 8, 0, 4, 7]
    self.target_status = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    self.initial_status = rand_status([1, 2, 3, 4, 5, 6, 7, 8, 0], 40)
    self.graph = Graph(self.initial_status)
    self.open.append(self.initial_status)
    self.idx = idx

  def h(self, idx, l):
    def h1(l):
      """
      8 puzzles

      mistaken number
      """
      count = 0
      for i in range(9):
        if self.target_status[i] != l[i] and l[i] != 0 and self.target_status[i] != 0:
          count += 1
      return count

    def h2(l):
      """
      8 puzzles

      manhatten distance
      """
      dis = 0
      for i in range(9):
        if self.target_status[i] == 0:
          continue
        w = -1
        for j in range(9):
          if self.target_status[i] == l[j]:
            w = j
            break
        dis += w // 3 + w % 3
      return dis
    def h3(l):
      """
      9 puzzles

      mistaken number
      """
      count = 0
      for i in range(9):
        if self.target_status[i] != l[i]:
          count += 1
      return count
    
    def h4(l):
      """
      9 puzzles

      manhattan distance
      """
      dis = 0
      for i in range(9):
        w = -1
        for j in range(9):
          if self.target_status[i] == l[j]:
            w = j
            break
        dis += w // 3 + w % 3
      return dis

    if idx == 1:
      return h1(l)
    elif idx == 2:
      return h2(l)
    elif idx == 3:
      return h3(l)
    else:
      return h4(l)

  def fn(self, idx, l):
    count = self.h(idx, l)
    depth = len(self.graph.paths[str(l)]) - 1
    return 0.8 * count + 0.2 * depth

  def search(self):
    index = self.idx
    if len(self.open) <= 0:
      return True, [], 0
    idx = 0
    _min = 99999
    for i in range(len(self.open)):
      if self.fn(index, self.open[i]) < _min:
        idx = i
        _min = self.fn(index, self.open[i])
      elif self.fn(index, self.open[i]) == _min and self.h(index, self.open[i]) < self.h(index, self.open[idx]):
        idx = i
        _min = self.fn(index, self.open[i])

    cur_status = copy.deepcopy(self.open[idx])
    self.open.pop(idx)
    self.closed.append(cur_status)
    if self.target_status == cur_status:
      return True, [], 0

    s_status = generate_subsequent_node(cur_status)
    M = []
    for sst in s_status:
      if self.h(index, cur_status) - self.h(index, sst) - 1 > 0 and index != 3:
        # judge the monotonicity of h
        print('h fail')
        exit(0)
        pass
      if not self.graph.is_prev_node(cur_status, sst):
        M.append(sst)
    
    for st in M:
      if (not(st in self.open)) and (not(st in self.closed)):
        self.open.append(st)
        self.graph.add(st, cur_status)
      else:
        self.graph.modify_path(st, cur_status)

    return False, cur_status, self.fn(1, cur_status)