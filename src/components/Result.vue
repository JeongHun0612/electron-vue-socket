<template>
  <v-container style="margin-left: 1px">
    <v-row>
      <v-card v-for="(item, index) in data" :key="index" width="145px">
        <ResultList
          :idx="index"
          :overTitle="item.overTitle"
          :domTitle="item.domTitle"
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
    return {};
  },
};
</script>