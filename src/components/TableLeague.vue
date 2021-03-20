<template>
  <div>
    <v-data-table
      id="league-list-table"
      :headers="headers"
      :items="data"
      :sort-by="['time', 'league']"
      height="500px"
      dense
      fixed-header
      disable-pagination
      hide-default-footer
      @click:row="rowClick"
      class="elevation-1"
    >
      <template v-slot:[`item.sport`]="{ item }">
        <v-icon color="orange"> {{ getSportIcon(item.sport) }} </v-icon>
      </template>
    </v-data-table>
  </div>
</template>

<script>
export default {
  props: ["data"],
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
          sortable: true,
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
    };
  },
  methods: {
    rowClick(idx) {
      this.$emit("rowClick", idx.id);
    },
    getSportIcon(sport) {
      switch (sport) {
        case "축구":
          return "mdi-soccer";
        case "농구":
          return "mdi-basketball";
        case "야구":
          return "mdi-baseball";
        case "하키":
          return "mdi-hockey-puck";
        case "배구":
          return "mdi-volleyball";
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
</style>