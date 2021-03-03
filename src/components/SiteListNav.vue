<template>
  <v-navigation-drawer v-model="drawer" app permanent width="250">
    <CurrentTime />
    <v-list class="pl-2" shaped>
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
import CurrentTime from './CurrentTime'

export default {
  components: { CurrentTime },
  data() {
    return {
      drawer: null,
      selected: true,
    };
  },
  methods: {
    siteAdd() {
      window.open("http://localhost:8080/#/siteAdd", "siteAdd", "width=1500");
      // this.$router.push({ name: 'SiteAdd' })
    },
  },
};
</script>
