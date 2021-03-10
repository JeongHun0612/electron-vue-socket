<template>
  <v-container style="margin-left: 1px">
    <v-row>
      <v-card
        v-for="(item, index) in data"
        :key="index"
        width="145px"
        style="border: 2px solid red"
      >
        <div class="result-list-header">
          <div class="grey lighten-2">
            {{ item.overTitle }}
          </div>
          <v-row no-gutters>
            <v-col sm="4">
              <div>123</div>
            </v-col>
            <v-col sm="4">
              <div>123</div>
            </v-col>
            <v-col sm="4">
              <div>123</div>
            </v-col>
          </v-row>
          <div class="grey lighten-2">
            {{ item.domTitle }}
          </div>
          <v-row no-gutters>
            <v-col sm="4">
              <div>123</div>
            </v-col>
            <v-col sm="4">
              <div>123</div>
            </v-col>
            <v-col sm="4">
              <div>123</div>
            </v-col>
          </v-row>
        </div>
        <div class="result-list-footer">
          <v-row no-gutters>
            <v-col sm="4">
              <div>
                <small>배팅금</small>
              </div>
            </v-col>
            <v-col sm="8">
              <div style="text-align: right">
                <small>500000</small>
              </div>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col sm="4">
              <div>
                <small>배팅금</small>
              </div>
            </v-col>
            <v-col sm="8">
              <div style="text-align: right">
                <small>500000</small>
              </div>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col sm="4">
              <div>
                <small>배팅금</small>
              </div>
            </v-col>
            <v-col sm="8">
              <div style="text-align: right">
                <small>500000</small>
              </div>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col sm="4">
              <div>
                <small>배팅금</small>
              </div>
            </v-col>
            <v-col sm="8">
              <div style="text-align: right">
                <small>500000</small>
              </div>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col sm="4">
              <div>
                <small>배팅금</small>
              </div>
            </v-col>
            <v-col sm="8">
              <div style="text-align: right">
                <small>500000</small>
              </div>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col sm="4">
              <div>
                <small>배팅금</small>
              </div>
            </v-col>
            <v-col sm="8">
              <div style="text-align: right">
                <small>500000</small>
              </div>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col sm="4">
              <div>
                <small>배팅금</small>
              </div>
            </v-col>
            <v-col sm="8">
              <div style="text-align: right; padding-bottom: 15px">
                <small>500000</small>
              </div>
            </v-col>
          </v-row>
        </div>
      </v-card>
    </v-row>
  </v-container>

  <!-- <v-card>
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
    </v-card> -->
</template>
<script>
export default {
  props: ["data"],

  data() {
    return {};
  },
};
</script>

<style>
.result-list-header div {
  text-align: center;
}

.result-list-footer div {
  text-align: center;
  height: 10px;
}

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