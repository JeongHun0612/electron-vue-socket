import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// import io from "socket.io-client";
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false
    // const socket = io.connect("http://192.168.219.150:50000", {
    //     reconnect: true,
    //     transports: ["websocket"],
    // });
    // Vue.prototype.$socket = socket

new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount('#app')