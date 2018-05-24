import Vue from 'vue'
import Router from 'vue-router'
import Tools from '@/components/Tools'
import Record from '@/components/Record'
import Probe from '@/components/Probe'
import About from '@/components/About'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Tools',
      component: Tools
    },
    {
      path: '/record',
      name: 'Record',
      component: Record
    },
    {
      path: '/probe',
      name: 'Probe',
      component: Probe
    },
    {
      path: '/about',
      name: 'About',
      component: About
    }
  ]
})
