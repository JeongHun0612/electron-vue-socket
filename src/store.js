import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        currentDomBet: "",
        domBet: "",
        currentDomWinnings: "",
        domWinnigs: "",
        siteData: [],
    },
    mutations: {
        getCurrentDomBet(state, payload) {
            state.currentDomBet = payload
        },
        getDomBet(state, payload) {
            state.domBet = payload;
        },
        getCurrentDomWinnigs(state, payload) {
            state.currentDomWinnings = payload;
        },
        getDomWinnigs(state, payload) {
            state.domWinnigs = payload;
        },
        getSiteData(state, payload) {
            state.siteData = payload
        }
    },
})