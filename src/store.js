import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        domBet: "",
        overBet: "",
        sites: [],
    },
    mutations: {
        getDomBet(state, payload) {
            state.domBet = payload;
        },
        getOverBet(state, payload) {
            state.overBet = payload;
        },
        getSites(state, payload) {
            state.sites = payload
        }
    },
})