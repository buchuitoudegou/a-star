from Astar import Astar

if __name__ == "__main__":
  astar = Astar()
  print(astar.open)
  search_times = 0
  last_num = 0
  input()
  while True:
    last_num = len(astar.open)
    complete, status, f_status = astar.search(2)
    search_times += 1
    if complete:
      break
    print(search_times)
    print('the number of nodes in open-table: %d' % len(astar.open))
    print('extension of the open-table: %d' % (len(astar.open) - last_num))
    print('search node: %s' % status)
    print('f(n): %f' % f_status)
    print('--------------------------------')
    
  print(astar.graph.paths[str(astar.target_status)])