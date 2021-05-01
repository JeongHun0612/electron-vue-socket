<template>
  <div>
    <NavDate />
    <div class="ma-2">
      <NavSite :data="siteListData" />
      <NavBet />
      <v-btn class="mt-3" color="primary" block @click="startBtn">
        <v-icon left size="25px"> mdi-arrow-right-drop-circle-outline</v-icon>
        분석 시작
      </v-btn>
    </div>
  </div>
</template>

<script>
import data from "@/data";
import NavDate from "./NavDate";
import NavSite from "./NavSite";
import NavBet from "./NavBet";
import { mapState, mapMutations } from "vuex";

export default {
  components: { NavDate, NavSite, NavBet },
  created() {
    this.$socket.emit("getSiteStatus");
    this.$socket.on("getSiteStatus", (res) => {
      this.siteListData = res;
    });

    // data test 버전
    // this.siteListData = data.siteListData;
  },
  data() {
    return {
      siteListData: [],
    };
  },
  computed: {
    ...mapState([
      "siteData",
      "currentDomBet",
      "currentDomWinnings",
      "isSnackBar",
    ]),
  },
  methods: {
    ...mapMutations(["setDomBet", "setDomWinnings", "setIsSnackBar"]),

    startBtn() {
      if (
        this.siteData.length != 0 &&
        this.currentDomBet != 0 &&
        this.currentDomWinnings != 0
      ) {
        this.setDomBet(this.currentDomBet);
        this.setDomWinnings(this.currentDomWinnings);

        this.$socket.emit("assignSite", this.siteData);
        this.$socket.on("assignSite", (res) => {
          console.log("assignSite");
        });
      } else {
        if (!this.isSnackBar) {
          this.setIsSnackBar(true);
          setTimeout(() => this.setIsSnackBar(false), 3000);
        }
      }
    },
  },
};
</script>

<style></style>
