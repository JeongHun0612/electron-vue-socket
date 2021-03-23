<template>
  <div>
    <NavDate />
    <NavSite :data="siteListData" />
    <NavBet />
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
    this.$socket.emit("getSiteStatus");
    this.$socket.on("getSiteStatus", (res) => {
      this.siteListData = res;
      // res.forEach((item, index) => {
      //   this.siteListData.push({
      //     status: item.status,
      //     siteName: item.siteName,
      //   });
      // });
      // this.siteListisRender = true;
    });
    // data test 버전
    // console.log(data.siteListData);
    // this.siteListData = data.siteListData;
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