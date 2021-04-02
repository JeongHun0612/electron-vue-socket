<template>
  <v-app id="inspire">
    <v-app-bar absolute clipped-right flat height="50"> </v-app-bar>

    <v-navigation-drawer app permanent width="250">
      <NavLeft />
    </v-navigation-drawer>

    <v-main class="pa-0">
      <Main />
    </v-main>
  </v-app>
</template>

<script>
import NavLeft from "../components/NavLeft";
import Main from "../components/Main";

export default {
  name: "Home",
  components: {
    Main,
    NavLeft,
  },
  created() {
    this.$socket.emit("connectSocket", this.user);
    this.$socket.on("connectSocket", (res) => {
      console.log(res);
    });

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
