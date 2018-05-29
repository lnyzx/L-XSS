import Vue from 'vue'
import App from './App'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Magic from './utils/magic'
import router from './router'
import store from './vuex/store'
import axios from 'axios'
import qs from 'qs'

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(Magic)
Vue.use(axios)
Vue.use(qs)
Vue.prototype.$axios = axios
Vue.prototype.$qs = qs

/* eslint-disable*/
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
  render: h => h(App)
})
