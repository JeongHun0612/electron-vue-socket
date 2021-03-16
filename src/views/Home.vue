<template>
  <v-app id="inspire">
    <v-app-bar absolute clipped-right flat height="50">
      <v-spacer></v-spacer>
      <Setting />
    </v-app-bar>

    <v-navigation-drawer app permanent width="230">
      <NavDate />
      <NavSite :data="siteListData" v-if="siteListisRender" />
    </v-navigation-drawer>

    <!-- <v-navigation-drawer app clipped permanent right>
      <v-list>
        <v-list-item v-for="n in 5" :key="n" link>
          <v-list-item-content>
            <v-list-item-title>Item {{ n }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer> -->

    <v-main class="pa-0">
      <Main />
    </v-main>
    <!-- <v-footer app inset> </v-footer> -->
  </v-app>
</template>

<script>
import NavSite from "../components/NavSite";
import NavDate from "../components/NavDate";
import Main from "../components/Main";
import Setting from "../components/Setting";

export default {
  name: "Home",
  components: {
    Main,
    NavSite,
    NavDate,
    Setting,
  },
  created() {
    this.$socket.emit("connectSocket");
    this.$socket.on("connectSocketResponse", (res) => {});

    this.$socket.emit("getSiteStatus");
    this.$socket.on("getSiteStatusResponse", (res) => {
      res.forEach((item, index) => {
        this.siteListData.push({
          status: item.status,
          siteName: item.siteName,
        });
      });
      this.siteListisRender = true;
    });
  },

  data() {
    return {
      siteListisRender: false,
      siteListData: [],
    };
  },
  computed: {},
  // methods: {
  //   siteAdd() {
  //     this.$router.push({ name: "setHome" });
  //   },
  // },
};
</script>