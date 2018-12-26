const puzzle = Vue.component('puzzle-comp', {
  props: ['bx', 'by'],
  template: '<span :style="\'background-position: \' + bx + \'px \' + by + \'px;\'"></span>'
});

const puzzleContainer = Vue.component('puzzle-wrapper', {
  components: { puzzle },
  props: ['status'],
  template: '<div style="height: 356px; width: 356px; position: relative; left: 50%; top: 50%;\
              transform: translate(-50%);">\
              <puzzle-comp v-for="(value, index) in status" v-bind:key="index" \
              :by="-((value - 1) - (value - 1) % 3) / 3 * 117" :bx="-(value - 1) % 3 * 117" v-if="value != 0" \
              class="puzzle"\
              :style="`left: ${index % 3 * 118}px; top: ${(index - index % 3) / 3 * 118}px;`"></puzzle-comp>\
            </div>'
});