from flask import Flask, render_template, jsonify
import service

app = Flask(__name__)

@app.route('/restart/<method>')
def restart(method):
  astar = service.astar.Astar(int(method))
  print(method)
  search_times = 0
  last_num = 0
  while True:
    complete, status, f_status = astar.search()
    search_times += 1
    print(search_times)
    print('the number of nodes in open-table: %d' % len(astar.open))
    print('extension of the open-table: %d' % (len(astar.open) - last_num))
    print('search node: %s' % status)
    print('f(n): %f' % f_status)
    print('--------------------------------')
    if complete:
      break
  result = astar.graph.paths[str(astar.target_status)]
  print(method)
  for i in range(len(result)):
    temp = result[i]
    for j in range(3):
     print(temp[j*3:j*3+3])
    if i != len(result) - 1:
      print('   ||  ')
      print('   \\/')
  return jsonify(status='OK',
                data=result)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(port=8080, debug=True)  