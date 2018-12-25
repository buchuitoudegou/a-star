from flask import Flask, render_template, jsonify
import service

app = Flask(__name__)

@app.route('/restart/<method>')
def restart(method):
  astar = service.astar.Astar(method)
  print('start')
  search_times = 0
  last_num = 0
  while True:
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
    if complete:
      break
  result = astar.graph.paths[str(astar.target_status)]
  return jsonify(status='OK',
                data=result)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(port=8080, debug=True)  