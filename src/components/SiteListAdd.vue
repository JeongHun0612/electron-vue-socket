<template>
  <div>
    <v-app-bar color="deep-purple accent-4" dense dark>
      <v-toolbar-title>환경설정</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer permanent width="250">
      <div class="pa-3">
        <v-text-field
          v-model="first"
          label="국내 배팅금 설정"
          outlined
        ></v-text-field>
      </div>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
};
</script>

<style>
</style>