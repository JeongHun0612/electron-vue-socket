<template>
  <v-list-item>
    <v-list-item-action>
      <v-checkbox v-model="isChecked"></v-checkbox>
    </v-list-item-action>
    <v-list-item-content>
      <v-list-item-title>{{ siteName }}</v-list-item-title>
    </v-list-item-content>
    <v-badge :color="getStatus" dot></v-badge>
  </v-list-item>
</template>

<script>
export default {
  props: ["idx", "siteName", "status"],
  data() {
    return { isChecked: 0 };
  },
  computed: {
    getStatus() {
      switch (this.status) {
        case 0:
          return "red darken-2";
        case 1:
          return "green darken-2";
      }
    },
  },
  watch: {
    isChecked(check) {
      console.log(check);
    },
  },
};
</script>
