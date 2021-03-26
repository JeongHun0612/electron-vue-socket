<template>
  <v-card>
    <v-card-subtitle>
      <span> 옵션 설정 </span>
    </v-card-subtitle>
    <v-card-text>
      <v-text-field
        v-model.lazy="domBet"
        v-money="money"
        label="국내 배팅금 설정"
        dense
        outlined
        append-icon="mdi-currency-krw"
        @input="setDomBet"
      ></v-text-field>

      <v-text-field
        v-model.lazy="domWinnigs"
        v-money="money"
        label="국내 당청금 설정"
        dense
        outlined
        append-icon="mdi-currency-krw"
        @input="setDomWinnigs"
      ></v-text-field>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapMutations } from "vuex";
import { VMoney } from "v-money";

export default {
  data() {
    return {
      domBet: "",
      domWinnigs: "",
      money: {
        decimal: "",
        thousands: "",
        precision: 0,
        masked: false,
      },
    };
  },
  directives: { money: VMoney },
  methods: {
    ...mapMutations(["getCurrentDomBet", "getCurrentDomWinnigs"]),

    setDomBet() {
      this.getCurrentDomBet(this.domBet);
    },
    setDomWinnigs() {
      this.getCurrentDomWinnigs(this.domWinnigs);
    },
  },
};
</script>