<template>
  <v-card>
    <v-card-subtitle> 국내 배팅금 설정 </v-card-subtitle>
    <v-card-text>
      <v-text-field
        v-model="domBet"
        label="국내 배팅금 설정"
        dense
        outlined
        @input="setDomBet"
      ></v-text-field>
      <v-text-field
        v-model="domWinnigs"
        label="국내 당청금 설정"
        dense
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
      domWinnigs: "",
    };
  },
  methods: {
    ...mapMutations(["getDomBet", "getDomWinnigs"]),
    setDomBet() {
      this.getDomBet(this.domBet);
    },
  },
};
</script>