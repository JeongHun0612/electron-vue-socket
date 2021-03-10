<template>
  <v-data-table
    id="league-list-table"
    :headers="headers"
    :items="items"
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
</template>

<script>
export default {
  created() {
    this.$socket.emit("getSite");

    // this.$socket.on("getSiteResponse", (res) => {
    //   console.log(res);
    // });

    // this.$socket.on("getSiteInfoResponse", (res, err) => {
    //   this.items = res.data;
    // });

    this.$socket.emit("getGameInfoBySiteName", this.sites);
    this.$socket.on("getGameInfoBySiteNameResponse", (res) => {
      res.forEach((item) => {
        this.items = this.items.concat(item.data);
      });
    });

    // this.$socket.emit("getAvailableSite", (req) => {});
    // this.$socket.on("getAvailableSiteResponse", (res) => {
    //   console.log(res);
    // });

    this.$socket.emit("getAvailableSiteInfo");
  },
  data() {
    return {
      sites: ["pista", "토타임"],
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
    rowClick(idx) {
      console.log(idx);
    },
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