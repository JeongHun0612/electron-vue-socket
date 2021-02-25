<template>
  <v-data-table
    id="league-list-table"
    :headers="headers"
    :items="desserts"
    height="500px"
    fixed-header
    disable-sort
    disable-pagination
    hide-default-footer
    @click="click"
    class="elevation-1"
  >
    <template v-slot:item.click="{ item }">
      <v-btn v-model="item.click">선택</v-btn>
    </template>
  </v-data-table>
</template>

<script>
export default {
  created() {
    // this.$socket.emit("getSiteInfo");
    // this.$socket.on("getSiteInfoResponse", (res) => {
    //   this.desserts = res.data;
    // });
  },
  methods: {
    click() {
      alert("msg");
    },
  },
  data() {
    return {
      headers: [
        {
          text: "경기시간",
          align: "center",
          divider: true,
          value: "name",
        },
        {
          text: "리그명",
          align: "center",
          divider: true,
          value: "calories",
        },
        {
          text: "홈팀",
          align: "center",
          divider: true,
          value: "fat",
        },
        {
          text: "원정팀",
          align: "center",
          divider: true,
          value: "carbs",
        },
        {
          text: "결과",
          align: "center",
          divider: true,
          value: "protein",
        },
        {
          text: "사이트명",
          align: "center",
          divider: true,
          value: "iron",
        },
        {
          text: "해외",
          align: "center",
          divider: true,
          value: "iron",
        },
        {
          text: "VS",
          align: "center",
          divider: true,
          value: "iron",
        },
        {
          text: "국내",
          align: "center",
          divider: true,
          value: "iron",
        },
        {
          text: "등록",
          align: "center",
          value: "click",
        },
      ],
      desserts: [
        {
          name: "Frozen",
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: "1%",
        },
        {
          name: "Ice cream",
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: "1%",
        },
        {
          name: "Eclair",
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: "7%",
        },
        {
          name: "Cupcake",
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: "8%",
        },
        {
          name: "Gingerbread",
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          iron: "16%",
        },
        {
          name: "Jelly bean",
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          iron: "0%",
        },
        {
          name: "Lollipop",
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          iron: "2%",
        },
        {
          name: "Honeycomb",
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          iron: "45%",
        },
        {
          name: "Donut",
          calories: 452,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          iron: "22%",
        },
        {
          name: "KitKat",
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          iron: "6%",
        },
        {
          name: "KitKat",
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          iron: "6%",
        },
      ],
    };
  },
};
</script>

<style>
    #league-list-table table thead tr th{
        background: gray;
    }
</style>