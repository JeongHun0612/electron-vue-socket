<template>
  <v-app id="inspire">
    <v-app-bar absolute clipped-right flat height="50">
      <v-spacer></v-spacer>
      <Setting />
    </v-app-bar>

    <v-navigation-drawer app permanent width="250">
      <NavLeft />
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
import NavLeft from "../components/NavLeft";
import Main from "../components/Main";
import Setting from "../components/Setting";

export default {
  name: "Home",
  components: {
    Main,
    NavLeft,
    Setting,
  },
  created() {
    this.$socket.emit("connectSocket", this.user);
    this.$socket.on("connectSocket", (res) => {
      console.log(res);
    });

    // this.$socket.emit("assignSite";
    // this.$socket.on("assignSite", (res) => {
    //   console.log("assignSite");
    // });

    this.$socket.emit("disconnect");
    this.$socket.on("disconnectResponse", (res) => {
      console.log("disconnectResponse");
    });
  },
  data() {
    return {
      user: {
        id: "1234",
        pw: "1234",
      },
    };
  },
};
</script>