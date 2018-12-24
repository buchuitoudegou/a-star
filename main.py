from Astar import Astar

if __name__ == "__main__":
  h = int(input('plz input the types of inspiration functions: \n\
  1: 8-puzzle problem. The number of mistaken puzzles.\n\
  2: 8-puzzle problem. Manhattan distance of each puzzle.\n\
  3: 9-puzzle problem. The number of mistaken puzzles.\n\
  4: 9-puzzle problem. Manhattan distance of each puzzle.\n'))
  astar = Astar(h)
  print(astar.open)
  search_times = 0
  last_num = 0
  # input()
  while True:
    last_num = len(astar.open)
    complete, status, f_status = astar.search()
    search_times += 1
    if complete:
      break
    print(search_times)
    print('the number of nodes in open-table: %d' % len(astar.open))
    print('extension of the open-table: %d' % (len(astar.open) - last_num))
    print('search node: %s' % status)
    print('f(n): %f' % f_status)
    print('--------------------------------')
    
  result = astar.graph.paths[str(astar.target_status)]
  for i in range(len(result)):
    temp = result[i]
    for j in range(3):
     print(temp[j*3:j*3+3])
    if i != len(result) - 1:
      print('   ||  ')
      print('   \\/')