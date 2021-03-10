<template>
  <v-app id="inspire">
    <v-app-bar absolute clipped-right flat height="50">
      <v-spacer></v-spacer>
      <!-- <v-btn class="mr-1" color="primary" @click="siteAdd()"> 환경 설정 </v-btn> -->

      <DialogSetting />
    </v-app-bar>

    <v-navigation-drawer app permanent width="230">
      <NavSite :data="siteListData" v-if="siteListisRender" />
      <NavDate />
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
      <TableLeague />
      <Result :data="resultData" />
    </v-main>
    <!-- <v-footer app inset> </v-footer> -->
  </v-app>
</template>

<script>
import NavSite from "../components/NavSite";
import NavDate from "../components/NavDate";
import TableLeague from "../components/TableLeague";
import Result from "../components/Result";
import DialogSetting from "../components/DialogSetting";

export default {
  name: "Home",
  components: {
    TableLeague,
    NavSite,
    Result,
    NavDate,
    DialogSetting,
  },
  created() {
    this.$socket.emit("getAvailableSite");
    this.$socket.on("getAvailableSiteResponse", (res) => {
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
      resultData: [
        {
          overTitle: "해외 승무패",
          domTitle: "국내 승무패",
        },
        {
          overTitle: "해외 0.0",
          domTitle: "국내 승무패",
        },
        {
          overTitle: "해외 0.1",
          domTitle: "국내 승무패",
        },
        {
          overTitle: "해외 0.2",
          domTitle: "국내 승무패",
        },
        {
          overTitle: "해외 0.3",
          domTitle: "국내 승무패",
        },
        {
          overTitle: "해외 0.4",
          domTitle: "국내 0.5",
        },
        {
          overTitle: "해외 0.5",
          domTitle: "국내 핸디",
        },
        {
          overTitle: "해외 0.6",
          domTitle: "국내 오버/언더",
        },
      ],
    };
  },
  methods: {
    siteAdd() {
      // window.open(
      //   "http://localhost:8081/#/siteAdd",
      //   "사이트 추가",
      //   "width=1500"
      // );
      this.$router.push({ name: "setHome" });
    },
  },
};
</script>