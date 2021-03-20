<template>
  <div class="result-list" style="padding: 1px">
    <div class="result-list-header">
      <div class="grey lighten-2">
        {{ this.overTitle }}
      </div>
      <v-row no-gutters class="grey lighten-3">
        <br />
        <v-col sm="4">
          <div>{{ this.overWin }}</div>
        </v-col>
        <v-col sm="4">
          <div>{{ this.overDraw }}</div>
        </v-col>
        <v-col sm="4">
          <div>{{ this.overLose }}</div>
        </v-col>
      </v-row>
      <div class="grey lighten-2">
        {{ domTitle }}
      </div>
      <v-row no-gutters class="grey lighten-3">
        <br />
        <v-col sm="4">
          <div>{{ this.domWin }}</div>
        </v-col>
        <v-col sm="4">
          <div>{{ this.domDraw }}</div>
        </v-col>
        <v-col sm="4">
          <div>{{ this.domLose }}</div>
        </v-col>
      </v-row>
    </div>
    <div class="result-list-footer">
      <v-row no-gutters dense>
        <v-col sm="4">
          <div class="grey lighten-2">배팅금</div>
        </v-col>
        <v-col sm="8">
          <div style="text-align: right">{{ domBet }}</div>
        </v-col>
      </v-row>
      <v-row no-gutters dense>
        <v-col sm="4">
          <div class="grey lighten-2">홈팀</div>
        </v-col>
        <v-col sm="8">
          <div style="text-align: right"></div>
        </v-col>
      </v-row>
      <v-row no-gutters dense>
        <v-col sm="4">
          <div class="grey lighten-2">무</div>
        </v-col>
        <v-col sm="8">
          <div style="text-align: right"></div>
        </v-col>
      </v-row>
      <v-row no-gutters dense>
        <v-col sm="4">
          <div class="grey lighten-2">원정</div>
        </v-col>
        <v-col sm="8">
          <div style="text-align: right"></div>
        </v-col>
      </v-row>
      <v-row no-gutters dense>
        <v-col sm="4">
          <div class="grey lighten-2">총액</div>
        </v-col>
        <v-col sm="8">
          <div style="text-align: right"></div>
        </v-col>
      </v-row>
      <v-row no-gutters dense>
        <v-col sm="4">
          <div class="grey lighten-2">당첨</div>
        </v-col>
        <v-col sm="8">
          <div style="text-align: right"></div>
        </v-col>
      </v-row>
      <v-row no-gutters dense>
        <v-col sm="4">
          <div class="grey lighten-2">결과</div>
        </v-col>
        <v-col sm="8">
          <div style="text-align: right"></div>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  props: [
    "idx",
    "overTitle",
    "overWin",
    "overDraw",
    "overLose",
    "domTitle",
    "domWin",
    "domDraw",
    "domLose",
  ],
  computed: {
    ...mapState(["domBet"]),
  },
  data() {
    return {
      result: {},
    };
  },
};
</script>

<style>
.result-list-header div {
  text-align: center;
}

.result-list-footer div {
  text-align: center;
  font-size: 14px;
  height: 20px;
}
</style>