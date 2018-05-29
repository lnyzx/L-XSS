/* eslint-disable*/
export default {
  install (Vue, option) {
    Vue.prototype.magic = function(value) {
        for (let shape of this.$store.state.shape) {
            if(shape === 'lower') {
                value = value.toLowerCase()
            } else if (shape === 'upper') {
                value = value.toUpperCase()
            } else if (shape === 'urlencode') {
                value = encodeURIComponent(value)
            }
        }
        return value
    }
  }
}