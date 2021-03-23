<template>
  <v-card class="ma-2">
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
      v-model="selected"
      :headers="headers"
      :items="data"
      :search="search"
      height="300px"
      dense
      item-key="siteName"
      show-select
      fixed-header
      disable-sort
      hide-default-footer
      class="elevation-1"
    >
      <template
        v-slot:[`item.data-table-select`]="{ item, isSelected, select }"
      >
        <v-simple-checkbox
          :value="isSelected"
          :disabled="!item.status"
          :ripple="false"
          color="primary"
          @input="select($event)"
        >
        </v-simple-checkbox>
      </template>
      <template v-slot:[`item.status`]="{ item }">
        <v-badge :color="getStatus(item.status)" dot></v-badge>
      </template>
    </v-data-table>
    <v-btn @click="test">test</v-btn>
  </v-card>
</template>

<script>
import { mapMutations } from "vuex";

export default {
  props: ["data"],
  created() {
    console.log(this.selected);
    if (this.selected.length != 0) {
      console.log("test");
    }
  },
  data() {
    return {
      search: "",
      selected: [],
      headers: [
        { text: "사이트명", align: "center", value: "siteName" },
        { text: "상태", align: "center", value: "status" },
      ],
      items: [],
      siteData: [],
    };
  },
  methods: {
    ...mapMutations(["getSites"]),

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
    test() {
      this.selected.forEach((item) => {
        this.siteData = this.siteData.concat(item.siteName);
      });
      console.log(this.siteData);
      this.$socket.emit("assignSite", this.siteData);
      this.$socket.on("assignSite", (res) => {
        console.log("assignSite");
      });
      this.getSites(this.sites);
    },
  },
};
</script>
