import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        domBet: "",
        domWinnigs: "",
        siteData: [],
    },
    mutations: {
        getDomBet(state, payload) {
            state.domBet = payload;
        },
        getDomWinnigs(state, payload) {
            state.domWinnigs = payload;
        },
        getSiteData(state, payload) {
            state.siteData = payload
        }
    },
})