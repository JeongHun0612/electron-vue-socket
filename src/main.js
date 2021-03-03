import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import io from "socket.io-client"
import vuetify from './plugins/vuetify'
import moment from 'moment'
import vueMoment from 'vue-moment'

const socket = io.connect("http://54.180.76.58:50000", {
    reconnect: true,
    transports: ["websocket"],
});

Vue.config.productionTip = false
Vue.use(vueMoment, moment)

Vue.prototype.$socket = socket

new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount('#app')