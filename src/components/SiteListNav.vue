<template>
  <v-navigation-drawer v-model="drawer" app width="300">
    <v-navigation-drawer
      v-model="drawer"
      absolute
      color="grey lighten-3"
      mini-variant
    >
    </v-navigation-drawer>

    <v-sheet color="grey lighten-5" height="72" width="100%"></v-sheet>

    <v-list class="pl-14" shaped>
      <v-btn block rounded @click="siteAdd">사이트추가</v-btn>
      <v-list-item v-for="n in 5" :key="n" link>
        <v-list-item-action>
          <v-checkbox v-model="selected"></v-checkbox>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>Item {{ n }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  data () {
    return {
      drawer: null,
      selected: true,
    };
  },
  methods: {
    siteAdd(){
      window.open("http://localhost:8080/#/siteAdd", "siteAdd", "width=500")
      // this.$router.push({ name: 'SiteAdd' })
    }
  }
};
</script>