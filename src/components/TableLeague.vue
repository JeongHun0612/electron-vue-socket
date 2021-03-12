<template>
  <div>
    <v-data-table
      id="league-list-table"
      :headers="headers"
      :items="data"
      height="500px"
      dense
      fixed-header
      sort-by="time"
      disable-pagination
      hide-default-footer
      @click:row="rowClick"
      class="elevation-1"
    >
      <template v-slot:[`item.sport`]="{ item }">
        <v-icon color="orange"> {{ getSportIcon(item.sport) }} </v-icon>
      </template>
    </v-data-table>
    <Result :data="resultData" />
  </div>
</template>

<script>
import Result from "./Result";

export default {
  components: { Result },
  props: ["data"],
  created() {},
  data() {
    return {
      items: [],
      headers: [
        {
          text: "종목",
          align: "center",
          divider: true,
          sortable: false,
          value: "sport",
        },
        {
          text: "경기시간",
          align: "center",
          divider: true,
          sortable: true,
          value: "time",
        },
        {
          text: "리그명",
          align: "center",
          divider: true,
          sortable: false,
          value: "league",
        },
        {
          text: "홈팀",
          align: "center",
          divider: true,
          sortable: false,
          value: "team1",
        },
        {
          text: "원정팀",
          align: "center",
          divider: true,
          sortable: false,
          value: "team2",
        },
        {
          text: "결과",
          align: "center",
          divider: true,
          sortable: false,
          value: "result",
        },
        {
          text: "사이트명",
          align: "center",
          divider: true,
          sortable: false,
          value: "site",
        },
        {
          text: "해외",
          align: "center",
          divider: true,
          sortable: false,
          value: "overseas",
        },
        {
          text: "VS",
          align: "center",
          divider: true,
          sortable: false,
          value: "vs",
        },
        {
          text: "국내",
          align: "center",
          divider: true,
          sortable: false,
          value: "domestic",
        },
      ],
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
    rowClick(idx) {},
    getSportIcon(sport) {
      switch (sport) {
        case "축구":
          return "mdi-soccer";
        case "농구":
          return "mdi-basketball";
        case "축구":
          return "mdi-baseball";
        case "하키":
          return "mdi-hockey-puck";
      }
    },
  },
};
</script>

<style>
#league-list-table {
  margin-top: 48px;
}

#league-list-table table thead tr th {
  background: rgb(187, 184, 184);
}

#league-list-table table tr td {
  height: 10px;
}
</style>