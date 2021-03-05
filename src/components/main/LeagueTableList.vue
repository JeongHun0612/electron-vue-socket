<template>
  <v-data-table
    id="league-list-table"
    :headers="headers"
    :items="items"
    height="500px"
    dense
    fixed-header
    :loading="loadTable"
    loading-text="Loading... Please wait"
    disable-pagination
    hide-default-footer
    @click:row="rowClick"
    class="elevation-1"
  >
    <template v-slot:item.sport="{ item }">
      <v-icon color="orange"> {{ getSportIcon(item.sport) }} </v-icon>
    </template>
  </v-data-table>
</template>

<script>
export default {
  created() {
    this.$socket.emit("getSiteInfo", (req) => {
      console.log("test");
    });

    this.$socket.on("getSiteInfoResponse", (res, err) => {
      this.loadTable = false;
      this.items = res.data.sort((a, b) => {
        return b.id - a.id;
      });
    });
  },
  data() {
    return {
      loadTable: true,
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
          value: "domain",
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
        {
          text: "등록",
          align: "center",
          sortable: false,
          value: "enrollment",
        },
      ],
    };
  },
  methods: {
    rowClick(item) {
      alert(item.id);
    },
    getSportIcon(sport) {
      if (sport == "축구") {
        return "mdi-soccer";
      } else if (sport == "농구") {
        return "mdi-basketball";
      } else if (sport == "야구") {
        return "mdi-baseball";
      } else if (sport == "하키") {
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