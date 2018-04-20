import Vue from 'vue'
import Router from 'vue-router'
import Resource from 'vue-resource'
import Skoobe from '@/components/Skoobe'

Vue.use(Router)
Vue.use(Resource)

export default new Router({
  routes: [
     {
      path: '/:search_query',
      name: 'Skoobe',
      component: Skoobe
    }
  ]
})
