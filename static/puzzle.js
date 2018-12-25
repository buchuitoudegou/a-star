const puzzle = Vue.component('puzzle-comp', {
  props: ['bx', 'by'],
  template: '<span :style="\'background-position: \' + bx + \'px \' + by + \'px;\'"></span>'
});

const puzzleContainer = Vue.component('puzzle-wrapper', {
  components: { puzzle },
  data() {
    return {
      status: [1, 2, 3, 4, 5, 6, 7, 8, 0]
    }
  },
  template: '<div>\
              <puzzle-comp v-for="(value, index) in status" v-bind:key="index" \
              :by="-((value - 1) - (value - 1) % 3) / 3 * 117" :bx="-(value - 1) % 3 * 117" v-if="value != 0" \
              class="puzzle"></puzzle-comp>\
            </div>'
});