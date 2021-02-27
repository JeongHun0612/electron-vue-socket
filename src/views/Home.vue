<template>
  <v-app id="inspire">
    <v-system-bar app>
      <v-spacer></v-spacer>
      <v-icon>mdi-square</v-icon>
      <v-icon>mdi-circle</v-icon>
      <v-icon>mdi-triangle</v-icon>
    </v-system-bar>

    <v-app-bar app clipped-right flat height="72">
      <v-spacer></v-spacer>

      <v-responsive max-width="156">
        <v-text-field
          dense
          flat
          hide-details
          rounded
          solo-inverted
        ></v-text-field>
      </v-responsive>
    </v-app-bar>

    <div class="site-list-nav">
      <SiteListNav />
    </div>

    <v-navigation-drawer app clipped permanent right>
      <v-list>
        <v-list-item v-for="n in 5" :key="n" link>
          <v-list-item-content>
            <v-list-item-title>Item {{ n }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main class="pa-0">
      <LeagueTableList />
    </v-main>

    <v-footer app color="transparent" height="73" inset>
      <v-text-field
        background-color="grey lighten-1"
        dense
        flat
        hide-details
        rounded
        solo
      ></v-text-field>
    </v-footer>
  </v-app>
</template>

<script>
import LeagueTableList from "../components/LeagueTableList";
import SiteListNav from "../components/SiteListNav";

export default {
  name: "Home",

  components: {
    LeagueTableList,
    SiteListNav,
  },
  created() {
    this.$socket.emit("getConnection ", (res) => {});
  },
  data() {
    return {};
  },
};
</script>
