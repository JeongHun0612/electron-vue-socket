<template>
  <v-card>
    <v-card-subtitle> 적용 사이트 선택 </v-card-subtitle>
    <v-card-text>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        dense
        single-line
        hide-details
      ></v-text-field>
    </v-card-text>
    <v-data-table
      :headers="headers"
      :items="data"
      :search="search"
      height="250px"
      dense
      fixed-header
      disable-sort
      hide-default-footer
      class="elevation-1"
    >
      <template v-slot:[`item.selected`]="{ item }">
        <v-simple-checkbox
          v-model="item.selected"
          :disabled="getDisabled(item.status)"
          :ripple="false"
          color="primary"
          @click="setSiteData"
        ></v-simple-checkbox>
      </template>

      <template v-slot:[`item.status`]="{ item }">
        <v-badge :color="getStatus(item.status)" dot></v-badge>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import { mapMutations } from "vuex";

export default {
  props: ["data"],
  data() {
    return {
      search: "",
      selected: [],
      headers: [
        { text: "선택", align: "center", value: "selected" },
        { text: "사이트명", align: "center", value: "siteName" },
        { text: "상태", align: "center", value: "status" },
      ],
      items: [],
      siteData: [],
    };
  },
  methods: {
    ...mapMutations(["getSiteData"]),

    getStatus(status) {
      switch (status) {
        case 0:
          return "red darken-2";
        case 1:
          return "green darken-2";
        case 2:
          return "yellow darken-2";
      }
    },
    getDisabled(status) {
      switch (status) {
        case 0:
          return true;
        case 1:
          return false;
        case 2:
          return true;
      }
    },
    setSiteData() {
      this.siteData = [];
      this.data.forEach((item) => {
        if (item.selected) this.siteData = this.siteData.concat(item.siteName);
      });
      this.$socket.emit("assignSite", this.siteData);
      this.$socket.on("assignSite", (res) => {
        console.log("assignSite");
      });
      this.getSiteData(this.siteData);
    },
  },
};
</script>
