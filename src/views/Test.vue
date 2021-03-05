<template>
  <v-app>
    <!-- <v-app-bar absolute></v-app-bar>
    <v-navigation-drawer app></v-navigation-drawer>
    <v-main>
      <v-container fluid>Hello Wolrd</v-container>
      <v-data-table class="ma-0"></v-data-table>
    </v-main> -->
  </v-app>
</template>

<script>
export default {
  created() {
    console.log(this.$vuetify.application.left);
    console.log("test");
  },
};
</script>

<style>
</style>