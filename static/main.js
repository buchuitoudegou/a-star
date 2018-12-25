window.onload = function() {
  const root = new Vue({
    el: '#puzzle',
    data: {
      status: [1,2,3,4,5,6,7,8,0],
      path: [[]],
      idx: 0,
      intervalId: 0
    },
    components: {
      puzzleContainer
    },
    methods: {
      restart() {
        const self = this;
        fetch('http://localhost:8080/restart/1').then((response) => {
          return response.json()
        }).then((res) => {
          console.log(res.data);
          self.path = res.data;
          self.status = self.path[0];
          self.idx = 0
        });
      },
      recover() {
        // if (idx + 1 < this.path.length) {
        //   this.status = this.path[++ idx];
        // }
        const self = this;
        this.intervalId = setInterval(function() {
          if (self.idx + 1 < self.path.length) {
            self.status = self.path[++ self.idx];
          } else {
            clearInterval(self.intervalId);
          }
        }, 1000);
      }
    } 
  });
  
}