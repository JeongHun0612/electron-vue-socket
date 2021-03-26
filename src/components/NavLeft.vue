<template>
  <div>
    <NavDate />
    <div class="ma-2">
      <NavSite :data="siteListData" />
      <NavBet />
    </div>
    <v-btn @click="test">분석 시작</v-btn>
  </div>
</template>

<script>
import data from "@/data";
import NavDate from "./NavDate";
import NavSite from "./NavSite";
import NavBet from "./NavBet";
import { mapState } from "vuex";

export default {
  components: { NavDate, NavSite, NavBet },
  created() {
    // this.$socket.emit("getSiteStatus");
    // this.$socket.on("getSiteStatus", (res) => {
    //   this.siteListData = res;
    // });

    // data test 버전
    this.siteListData = data.siteListData;
  },
  data() {
    return {
      siteListData: [],
    };
  },
  computed: {
    ...mapState(["siteData"]),
  },
  methods: {
    test() {
      if (this.siteData.length != 0) {
        console.log(this.siteData);
      }
    },
  },
};
</script>

<style>
</style>