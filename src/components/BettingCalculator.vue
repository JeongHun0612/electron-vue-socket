<template>
  <v-flex>
    <v-card height="100%">
      <div class="wdl-title">
        <span>{{ overWDL }}</span>
      </div>
      <div class="wdl-betting">
        <span class="ml-2"> {{ overWin }} </span>
        <span> {{ overDraw }} </span>
        <span class="mr-2"> {{ overLose }} </span>
      </div>
      <div class="wdl-title">
        <span> {{ domesticWDL }}</span>
      </div>
      <div class="wdl-betting">
        <span class="ml-2"> {{ domesticWin }} </span>
        <span> {{ domesticDraw }} </span>
        <span class="mr-2"> {{ domesticLose }} </span>
      </div>
      <div class="batting-result">
        <div>
          <span>배팅금</span>
        </div>
        <div>
          <span>홈팀</span>
        </div>
        <div>
          <span>무</span>
        </div>
        <div>
          <span>원정</span>
        </div>
        <div>
          <span>총액</span>
        </div>
        <div>
          <span>당첨</span>
        </div>
        <div>
          <span>결과</span>
        </div>
      </div>
    </v-card>
  </v-flex>
</template>
<script>
export default {
  props: [
    "overWDL",
    "overWin",
    "overDraw",
    "overLose",
    "domesticWDL",
    "domesticWin",
    "domesticDraw",
    "domesticLose",
  ],
};
</script>

<style>
.wdl-title {
  background-color: gray;
  text-align: center;
}
.wdl-betting,
.batting-result div {
  background-color: rgb(172, 170, 170);
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.batting-result div span {
  width: 50px;
  background-color: rgb(129, 126, 126);
  text-align: center;
}
</style>