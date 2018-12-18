import copy

class Graph():
  """
  description: a graph that contain every shortest path from source to each node 

  :attribute paths: a list of the shortest path from s0 to every node p

  :attribute type: path is a list containing nodes in the path. paths is a dict containing paths
  """
  def __init__(self, s0):
    """
    :param s0: the source of the graph
    """
    self.s0 = s0
    self.paths = {}
    self.paths[str(s0)] = [s0]
  
  def is_prev_node(self, src, dst):
    """
    description: is dst src's prev node
    """
    if not str(src) in self.paths:
      return False
    path = self.paths[str(src)]
    for status in path:
      if status == dst:
        return True
    return False
  
  def is_in_graph(self, st):
    return (str(st) in self.paths) 
  
  def add(self, new_st, prev_st):
    if str(new_st) in self.paths:
      return
    if not str(prev_st) in self.paths:
      return
    new_path = copy.deepcopy(self.paths[str(prev_st)])
    self.paths[str(new_st)] = new_path + [new_st]
  
  def modify_path(self, src, new_prev):
    if not str(new_prev) in self.paths:
      return
    origin_path = self.paths[str(src)]
    new_path = self.paths[str(new_prev)] + [src]
    if len(origin_path) > len(new_path):
      self.paths[str(src)] = new_path
