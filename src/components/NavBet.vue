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
        v-model.lazy="domWinnings"
        v-money="money"
        label="국내 당청금 설정"
        dense
        outlined
        append-icon="mdi-currency-krw"
        @input="setDomWinnings"
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
      domWinnings: "",
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
    ...mapMutations(["setCurrentDomBet", "setCurrentDomWinnings"]),

    setDomBet() {
      this.setCurrentDomBet(this.domBet);
    },
    setDomWinnings() {
      this.setCurrentDomWinnings(this.domWinnings);
    },
  },
};
</script>
