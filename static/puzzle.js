const puzzle = Vue.component('puzzle-comp', {
  props: ['bx', 'by'],
  template: '<span :style="\'background-position: \' + bx + \'px \' + by + \'px;\'"></span>'
});

const puzzleContainer = Vue.component('puzzle-wrapper', {
  components: { puzzle },
  props: ['status'],
  template: '<div>\
              <puzzle-comp v-for="(value, index) in status" v-bind:key="index" \
              :by="-((value - 1) - (value - 1) % 3) / 3 * 117" :bx="-(value - 1) % 3 * 117" v-if="value != 0" \
              class="puzzle"\
              :style="`left: ${index % 3 * 117}px; top: ${(index - index % 3) / 3 * 117}px;`"></puzzle-comp>\
            </div>'
});