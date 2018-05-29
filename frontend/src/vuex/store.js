/* eslint-disable */
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    strict: false,
    state: {
        hexAdd0x: false,
        shape: [],
        randomRange: ['upper', 'lower', 'number']
    },
    mutations: {
        cycle0x: state => state.hexAdd0x = !state.hexAdd0x,
        changeShape (state, shape) {
            state.shape = shape
        },
        changeRandomRange (state, range) {
            state.randomRange = range
        }
    }
})