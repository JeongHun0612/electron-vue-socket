<template>
  <v-data-table
    id="league-list-table"
    :headers="headers"
    :items="items"
    height="500px"
    fixed-header
    disable-sort
    disable-pagination
    hide-default-footer
    @click:row="rowClick"
    class="elevation-1"
  >
    <template v-slot:item.sport="{ item }">
      <v-icon>mdi-tennis</v-icon>
    </template>
  </v-data-table>
</template>

<script>
export default {
  created() {
    this.$socket.emit("getSiteInfo", (req) => {
      console.log("test")
    })

    this.$socket.on("getSiteInfoResponse", (res) => {
      this.items = res.data;
      console.log(res.data[0].id);
    });
  },
  methods: {
    rowClick(item) {
      alert(item.id);
    },
    getSportImage(sport) {
      if ((sport = "축구")) {
      }
    },
  },
  data() {
    return {
      headers: [
        {
          text: "종목",
          align: "center",
          divider: true,
          value: "sport",
        },
        {
          text: "경기시간",
          align: "center",
          divider: true,
          value: "time",
        },
        {
          text: "리그명",
          align: "center",
          divider: true,
          value: "league",
        },
        {
          text: "홈팀",
          align: "center",
          divider: true,
          value: "team1",
        },
        {
          text: "원정팀",
          align: "center",
          divider: true,
          value: "team2",
        },
        {
          text: "결과",
          align: "center",
          divider: true,
          value: "result",
        },
        {
          text: "사이트명",
          align: "center",
          divider: true,
          value: "domain",
        },
        {
          text: "해외",
          align: "center",
          divider: true,
          value: "overseas",
        },
        {
          text: "VS",
          align: "center",
          divider: true,
          value: "vs",
        },
        {
          text: "국내",
          align: "center",
          divider: true,
          value: "domestic",
        },
        {
          text: "등록",
          align: "center",
          value: "enrollment",
        },
      ],
      items: [],
    };
  },
};
</script>

<style>
#league-list-table table thead tr th {
  background: gray;
}
</style>