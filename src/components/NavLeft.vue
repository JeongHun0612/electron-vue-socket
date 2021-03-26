<template>
  <div>
    <NavDate />
    <div class="ma-2">
      <NavSite :data="siteListData" />
      <NavBet />
    </div>
    <v-btn>btn</v-btn>
  </div>
</template>

<script>
import data from "@/data";
import NavDate from "./NavDate";
import NavSite from "./NavSite";
import NavBet from "./NavBet";

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
};
</script>

<style>
</style>