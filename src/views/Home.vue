<template>
  <v-app id="inspire">
    <!-- <v-system-bar absolute>
      <v-spacer></v-spacer>
      <v-icon>mdi-square</v-icon>
      <v-icon>mdi-circle</v-icon>
      <v-icon>mdi-triangle</v-icon>
    </v-system-bar> -->

    <v-app-bar absolute clipped-right flat height="50"> </v-app-bar>

    <v-navigation-drawer app permanent width="230">
      <SiteListNav />
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
      <LeagueTableList />
      <v-container class="mt-1" fluid>
        <v-layout row>
          <BettingCalculator
            v-for="calc in calculator"
            :key="calc.id"
            :overWDL="calc.overWDL"
            :overWin="calc.overWin"
            :overDraw="calc.overDraw"
            :overLose="calc.overLose"
            :domesticWDL="calc.domesticWDL"
            :domesticWin="calc.domesticWin"
            :domesticDraw="calc.domesticDraw"
            :domesticLose="calc.domesticLose"
          />
        </v-layout>
      </v-container>
    </v-main>
    <!-- <v-footer app inset> </v-footer> -->
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
        {
          overWDL: "해외 승무패",
          overWin: "2.14",
          overDraw: "P3.6",
          overLose: "P3.43",
          domesticWDL: "국내 승무패",
          domesticWin: "2.45",
          domesticDraw: "3.12",
          domesticLose: "2.55",
        },
        {
          overWDL: "해외 0.0",
          overWin: "2.14",
          overDraw: "P3.6",
          overLose: "P3.43",
          domesticWDL: "국내 승무패",
          domesticWin: "2.45",
          domesticDraw: "3.12",
          domesticLose: "2.55",
        },
        {
          overWDL: "해외 0.1",
          overWin: "2.14",
          overDraw: "P3.6",
          overLose: "P3.43",
          domesticWDL: "국내 승무패",
          domesticWin: "2.45",
          domesticDraw: "3.12",
          domesticLose: "2.55",
        },
        {
          overWDL: "해외 0.2",
          overWin: "2.14",
          overDraw: "P3.6",
          overLose: "P3.43",
          domesticWDL: "국내 승무패",
          domesticWin: "2.45",
          domesticDraw: "3.12",
          domesticLose: "2.55",
        },
        {
          overWDL: "해외 0.3",
          overWin: "2.14",
          overDraw: "P3.6",
          overLose: "P3.43",
          domesticWDL: "국내 승무패",
          domesticWin: "2.45",
          domesticDraw: "3.12",
          domesticLose: "2.55",
        },
        {
          overWDL: "해외 0.4",
          overWin: "2.14",
          overDraw: "P3.6",
          overLose: "P3.43",
          domesticWDL: "국내 0.5",
          domesticWin: "2.45",
          domesticDraw: "3.12",
          domesticLose: "2.55",
        },
        {
          overWDL: "해외 0.5",
          overWin: "2.14",
          overDraw: "P3.6",
          overLose: "P3.43",
          domesticWDL: "국내 핸디",
          domesticWin: "2.45",
          domesticDraw: "3.12",
          domesticLose: "2.55",
        },
        {
          overWDL: "해외 0.6",
          overWin: "2.14",
          overDraw: "P3.6",
          overLose: "P3.43",
          domesticWDL: "국내 오버/언더",
          domesticWin: "2.45",
          domesticDraw: "3.12",
          domesticLose: "2.55",
        },
      ],
    };
  },
};
</script>