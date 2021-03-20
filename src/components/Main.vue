<template>
  <div>
    <TableLeague :data="tableListData" v-on:rowClick="getResultData" />
    <Result :data="resultData" />
  </div>
</template>

<script>
import TableLeague from "./TableLeague";
import Result from "./Result";
import data from "@/data";

export default {
  components: { TableLeague, Result },
  created() {
    this.$socket.emit("getGameInfoBySiteName", this.sites);
    this.$socket.on("getGameInfoBySiteNameResponse", (res) => {
      this.tableListData = [];
      res.forEach((item) => {
        this.tableListData = this.tableListData.concat(item.data);
      });
    });

    this.$socket.emit("getSiteInfo", this.sites);
    this.$socket.on("getSiteInfoResponse", (res) => {
      this.tableListData = [];
      res.forEach((item) => {
        this.tableListData = this.tableListData.concat(item.data);
      });
    });

    // data test 버전
    this.tableListData = data.tableListData;
    for (let i = 0; i < data.tableListData.length; i++) {
      this.tableListData[i].id = i;
    }
  },
  data() {
    return {
      sites: ["토타임", "pista"],
      tableListData: [],
      resultData: [],
    };
  },
  methods: {
    getResultData(idx) {
      console.log("부모 : " + idx);
      this.resultData = this.tableListData[idx].data;
    },
  },
};
</script>