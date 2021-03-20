<template>
  <div>
    <NavDate />
    <NavSite :data="siteListData" v-if="siteListisRender" />
  </div>
</template>

<script>
import data from "@/data";
import NavDate from "./NavDate";
import NavSite from "./NavSite";

export default {
  components: { NavDate, NavSite },
  created() {
    this.$socket.emit("getSiteStatus");
    this.$socket.on("getSiteStatusResponse", (res) => {
      res.forEach((item, index) => {
        this.siteListData.push({
          status: item.status,
          siteName: item.siteName,
        });
      });
      this.siteListisRender = true;
    });

    // data test 버전
    this.siteListData = data.siteListData;
  },
  data() {
    return {
      siteListisRender: true,
      siteListData: [],
    };
  },
};
</script>

<style>
</style>