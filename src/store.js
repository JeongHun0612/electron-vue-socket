import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    currentDomBet: "",
    domBet: "0",
    currentDomWinnings: "",
    domWinnings: "0",

    siteData: [],

    isSnackBar: false,
    timeout: 2000,
  },
  mutations: {
    setCurrentDomBet(state, payload) {
      state.currentDomBet = payload;
    },
    setDomBet(state, payload) {
      state.domBet = payload;
    },
    setCurrentDomWinnings(state, payload) {
      state.currentDomWinnings = payload;
    },
    setDomWinnings(state, payload) {
      state.domWinnings = payload;
    },
    setSiteData(state, payload) {
      state.siteData = payload;
    },
    setIsSnackBar(state, payload) {
      state.isSnackBar = payload;
    },
  },
  getters: {
    getDomBet: (state) => {
      return state.domBet;
    },
    getDomWinningsBet: (state) => {
      return state.domWinnings;
    },
  },
});
