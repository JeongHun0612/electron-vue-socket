<template>
  <v-card class="ma-2">
    <v-card-subtitle> 배팅금 설정 </v-card-subtitle>
    <v-card-text>
      <v-text-field
        v-model="domBet"
        label="국내 배팅금 설정"
        dense
        clearable
        outlined
      ></v-text-field>
      <v-text-field
        v-model="overBet"
        dense
        label="국내 당청금 설정"
        clearable
        outlined
      ></v-text-field>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapMutations } from "vuex";

export default {
  data() {
    return {
      domBet: "",
      overBet: "",
    };
  },
  methods: {
    ...mapMutations(["getDomBet", "getOverBet"]),
    Setting() {
      this.getDomBet(this.domBet);
    },
  },
};
</script>