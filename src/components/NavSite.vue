<template>
  <!-- <v-list class="pl-2" shaped v-for="(item, index) in data" :key="index">
      <NavSiteList
        :idx="index"
        :siteName="item.siteName"
        :status="item.status"
      ></NavSiteList>
    </v-list> -->
  <v-card class="ma-2">
    <v-card-title>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        dense
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
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
    <v-btn @click="test">btn</v-btn>
  </v-card>
</template>

<script>
import NavSiteList from "./NavSiteList";

export default {
  components: { NavSiteList },
  props: ["data"],
  created() {},
  data() {
    return {
      search: "",
      selected: [],
      headers: [
        { text: "사이트명", align: "center", value: "siteName" },
        { text: "상태", align: "center", value: "status" },
      ],
      items: [],
    };
  },

  methods: {
    getStatus(status) {
      switch (status) {
        case false:
          return "red darken-2";
        case true:
          return "green darken-2";
      }
    },
    test() {
      console.log(this.selected);
    },
    isSelectable() {
      console.log("test");
    },
  },
};
</script>
