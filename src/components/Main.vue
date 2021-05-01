<template>
  <div>
    <TableLeague :data="tableListData" v-on:rowClick="getResultData" />
    <Result :data="resultData" />
    <v-snackbar v-model="isSnackBar" :timeout="timeout" top>
      <v-icon class="mr-2" color="red"> mdi-alert </v-icon>
      사이트와 배팅금을 설정해주세요.
    </v-snackbar>
  </div>
</template>

<script>
import TableLeague from "./TableLeague";
import Result from "./Result";
import data from "@/data";
import { mapMutations, mapState } from "vuex";

export default {
  components: { TableLeague, Result },
  created() {
    this.$socket.emit("getSiteInfo");
    this.$socket.on("getSiteInfo", (res) => {
      this.tableListData = res;
      for (let i = 0; i < this.tableListData.length; i++) {
        this.tableListData[i].id = i;
      }
    });

    this.$socket.emit("getResultData");
    this.$socket.on("getResultData", (res) => {
      this.tableListData = [];
      res.forEach((item) => {
        this.tableListData = this.tableListData.concat(item.data);
      });
    });

    // data test 버전
    // this.tableListData = data.tableListData;
    // for (let i = 0; i < data.tableListData.length; i++) {
    //   this.tableListData[i].id = i;
    // }
  },
  data() {
    return {
      tableListData: [],
      resultData: ["", "", "", "", "", "", "", ""],
    };
  },
  computed: {
    ...mapState(["isSnackBar", "timeout"]),
  },
  methods: {
    ...mapMutations(["setIsSnackBar"]),

    getResultData(idx) {
      console.log("부모 : " + idx);
      // this.resultData = this.tableListData[idx];
    },
  },
};
</script>
