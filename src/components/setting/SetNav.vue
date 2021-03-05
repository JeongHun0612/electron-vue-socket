<template>
  <div class="pa-3">
    <v-text-field
      v-model="domesticBet"
      label="국내 배팅금 설정"
      dense
      append-outer-icon="mdi-currency-krw"
      clearable
      outlined
    ></v-text-field>
    <v-text-field
      v-model="overseasBet"
      dense
      label="해외 배팅금 설정"
      append-outer-icon="mdi-currency-krw"
      clearable
      outlined
    ></v-text-field>
    <v-btn color="primary" width="194px"> 설정 저장 </v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return {
      domesticBet: "",
      overseasBet: "",
    };
  },
};
</script>

<style>
</style>