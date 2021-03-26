<template>
  <v-card>
    <v-card-subtitle> 국내 배팅금 설정 </v-card-subtitle>
    <v-card-text>
      <v-text-field
        v-model="domBet"
        label="국내 배팅금 설정"
        dense
        outlined
        height="5"
        append-outer-icon="mdi-currency-krw"
      ></v-text-field>
      <v-text-field
        v-model="overBet"
        label="국내 당청금 설정"
        dense
        outlined
        append-outer-icon="mdi-currency-krw"
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