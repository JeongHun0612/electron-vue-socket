<template>
  <v-app id="inspire">
    <v-system-bar app>
      <v-spacer></v-spacer>
      <v-icon>mdi-square</v-icon>
      <v-icon>mdi-circle</v-icon>
      <v-icon>mdi-triangle</v-icon>
    </v-system-bar>

    <v-app-bar app clipped-right flat height="50"> </v-app-bar>

    <div class="site-list-nav">
      <SiteListNav />
    </div>

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
      <LeagueTableList />
      <v-container mt-1 fluid>
        <v-layout wrap row>
          <BettingCalculator
            v-for="calc in calculator"
            :key="calc.name"
            :name="calc.name"
          />
        </v-layout>
      </v-container>
    </v-main>

    <v-footer app color="transparent" height="10" inset> </v-footer>
  </v-app>
</template>

<script>
import LeagueTableList from "../components/LeagueTableList";
import SiteListNav from "../components/SiteListNav";
import BettingCalculator from "../components/BettingCalculator";

export default {
  name: "Home",

  components: {
    LeagueTableList,
    SiteListNav,
    BettingCalculator,
  },
  data() {
    return {
      calculator: [
        { name: "해외 승무패", overWin: "2.14", overDraw: "P3.6", overLose: "P3.43" },
        { name: "해외 0.0" },
        { name: "해외 0.1" },
        { name: "해외 0.2" },
        { name: "해외 0.3" },
        { name: "해외 0.4" },
        { name: "해외 0.5" },
        { name: "해외 0.6" },
      ],
    };
  },
};
</script>
