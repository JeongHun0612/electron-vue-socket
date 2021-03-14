<template>
  <div>
    <TableLeague :data="tableListData"/>
    <Result :data="resultData" />
  </div>
</template>

<script>
import TableLeague from "./TableLeague";
import Result from "./Result";

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
  },
  data() {
    return {
    sites: ['토타임', 'pista'],
      tableListData: [],
      resultData: [
        {
          overTitle: "해외 승무패",
          domTitle: "국내 승무패",
          overWin: "",
          overDraw: "",
          overLose: "",
          domWin: "",
          domDraw: "",
          domLose: "",
        },
        {
          overTitle: "해외 0.0",
          domTitle: "국내 승무패",
          overWin: "",
          overDraw: "",
          overLose: "",
          domWin: "",
          domDraw: "",
          domLose: "",
        },
        {
          overTitle: "해외 0.25",
          domTitle: "국내 승무패",
          overwin: "",
          overDraw: "",
          overLose: "",
          domWin: "",
          domDraw: "",
          domLose: "",
        },
        {
          overTitle: "해외 0.5",
          domTitle: "국내 승무패",
          overWin: "",
          overDraw: "",
          overLose: "",
          domWin: "",
          domDraw: "",
          domLose: "",
        },
        {
          overTitle: "해외 0.75",
          domTitle: "국내 승무패",
          overWin: "",
          overDraw: "",
          overLose: "",
          domWin: "",
          domDraw: "",
          domLose: "",
        },
        {
          overTitle: "해외 승무패",
          domTitle: "국내 0.5",
          overWin: "",
          overDraw: "",
          overLose: "",
          domWin: "",
          domDraw: "",
          domLose: "",
        },
        {
          overTitle: "해외 핸디",
          domTitle: "국내 핸디",
          overWin: "",
          overDraw: "",
          overLose: "",
          domWin: "",
          domDraw: "",
          domLose: "",
        },
        {
          overTitle: "해외 오버/언더",
          domTitle: "국내 오버/언더",
          overWin: "",
          overDraw: "",
          overLose: "",
          domWin: "",
          domDraw: "",
          domLose: "",
        },
      ],
    };
  },
  methods: {
  },
};
</script>