<template>
  <div>
    <v-app-bar color="deep-purple accent-4" dense dark> </v-app-bar>

    <v-navigation-drawer app permanent width="250">
      <CurrentTime />
      <SetNav />
    </v-navigation-drawer>

    <div>
      <v-form>
        <v-container ml-2 fluid max-width="80%">
          <v-row class="site_add_list_header">
            <!-- <span>0.</span> -->
            <v-col lg="2">
              <v-text-field
                value="기본 사이트 주소"
                dense
                readonly
                rounded
              ></v-text-field>
            </v-col>
            <v-col lg="1">
              <v-text-field
                value="사이트명"
                dense
                readonly
                rounded
              ></v-text-field>
            </v-col>
            <v-col lg="1">
              <v-text-field
                value="아이디"
                dense
                readonly
                rounded
              ></v-text-field>
            </v-col>
            <v-col lg="1">
              <v-text-field
                value="비밀번호"
                dense
                readonly
                rounded
              ></v-text-field>
            </v-col>
            <v-col lg="2">
              <v-text-field
                value="변경된 주소"
                dense
                readonly
                rounded
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row class="site_add_list" v-for="n in 5" :key="n">
            <span>{{ n + "." }}</span>
            <v-col lg="2">
              <v-text-field outlined dense></v-text-field>
            </v-col>
            <v-col lg="1">
              <v-text-field outlined dense></v-text-field>
            </v-col>
            <v-col lg="1">
              <v-text-field outlined dense></v-text-field>
            </v-col>
            <v-col lg="1">
              <v-text-field outlined dense></v-text-field>
            </v-col>
            <v-col lg="2">
              <v-text-field outlined dense></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </div>
  </div>
</template>

<script>
import CurrentTime from "../CurrentTime.vue";
import SetNav from "./SetNav.vue";

export default {
  name: "setHome",
  components: { CurrentTime, SetNav },
  data() {
    return {
      settingInput: [],
    };
  },
};
</script>

<style>
.site_add_list_header {
  height: 50px;
}

.site_add_list {
  height: 50px;
}

.site_add_list span {
  margin-top: 20px;
  color: blue;
}
</style>