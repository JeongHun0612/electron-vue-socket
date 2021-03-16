<template>
  <div>
    <TableLeague :data="tableListData" />
  </div>
</template>

<script>
import TableLeague from "./TableLeague";
import data from "@/data";

export default {
  components: { TableLeague },
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

    this.tableListData = data.tableListData;
    for (let i = 0; i < data.tableListData.length; i++) {
      this.tableListData[i].id = i;
    }

    console.log(this.tableListData);
  },
  data() {
    return {
      sites: ["토타임", "pista"],
      tableListData: [],
    };
  },
};
</script>