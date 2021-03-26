<template>
  <v-container fluid>
    <v-row>
      <v-card v-for="(item, index) in data" :key="index" width="165.7px">
        <ResultList
          :style="getTest(index)"
          :idx="index"
          :overTitle="overTitle[index]"
          :domTitle="domTitle[index]"
          :overWin="item.overWin"
          :overDraw="item.overDraw"
          :overLose="item.overLose"
          :domWin="item.domWin"
          :domDraw="item.domDraw"
          :domLose="item.domLose"
        ></ResultList>
      </v-card>
    </v-row>
  </v-container>
</template>
<script>
import ResultList from "./ResultList";

export default {
  components: { ResultList },
  props: ["data"],

  data() {
    return {
      overTitle: [
        "해외 승무패",
        "해외 0.0",
        "해외 0.25",
        "해외 0.5",
        "해외 0.7",
        "해외 승무패",
        "해외 핸디",
        "해외 오버/언더",
      ],
      domTitle: [
        "국내 승무패",
        "국내 승무패",
        "국내 승무패",
        "국내 승무패",
        "국내 승무패",
        "국내 0.5",
        "국내 핸디",
        "국내 오버/언더",
      ],
      max: 0,
    };
  },
  methods: {
    getTest(idx) {
      if (this.data[idx].result > this.max) {
        this.max = this.data[idx].result;
      }
      if (this.max == this.data[idx].result) {
        return "border: 4px solid red";
      }
    },
  },
};
</script>