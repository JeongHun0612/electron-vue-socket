import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import SiteListAdd from '@/components/SiteListAdd.vue'

Vue.use(Router)

export default new Router({
    routes: [{
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/siteAdd',
            name: 'SiteAdd',
            component: SiteListAdd
        }
    ]
})