<template>
  <v-sheet class="pa-2" color="grey lighten-5" height="50" width="100%">
    <span class="date-text"> {{ date }} </span>
    <span class="time-text"> {{ time }} </span>
  </v-sheet>
</template>

<script>
export default {
  created() {
    this.date = this.$moment().format("M월 d일");
    setInterval(() => {
      this.time = this.$moment().format("HH:mm:ss");
    }, 1000);
  },
  data() {
    return {
      time: "00:00:00",
      date: "0월 0일",
    };
  },
};
</script>

<style>
.date-text {
  color: blue;
  margin-left: 20px;

  font-size: 23px;
  font-weight: bold;
}

.time-text {
  margin-left: 10px;

  font-size: 23px;
  font-weight: bold;
}
</style>