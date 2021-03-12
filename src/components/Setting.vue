<template>
  <v-dialog v-model="dialog" persistent max-width="400px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="primary" dark v-bind="attrs" v-on="on"> Open Dialog </v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="headline">User Profile</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col md="12">
              <v-text-field
                v-model="domBet"
                label="국내 배팅금 설정"
                dense
                append-outer-icon="mdi-currency-krw"
                clearable
                outlined
              ></v-text-field
            ></v-col>
            <v-col md="12">
              <v-text-field
                v-model="overBet"
                dense
                label="해외 배팅금 설정"
                append-outer-icon="mdi-currency-krw"
                clearable
                outlined
              ></v-text-field
            ></v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="dialog = false"> 닫기 </v-btn>
        <v-btn color="blue darken-1" text @click="Setting()"> 저장 </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapMutations } from "vuex";

export default {
  data() {
    return {
      dialog: false,
      domBet: "",
      overBet: "",
    };
  },

  methods: {
    ...mapMutations(["getDomBet", "getOverBet"]),
    Setting() {
      this.getDomBet(this.domBet);
      this.dialog = false;
    },
  },
};
</script>

<style>
</style>