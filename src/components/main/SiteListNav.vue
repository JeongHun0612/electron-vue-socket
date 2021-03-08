<template>
  <div>
    <CurrentTime />
    <v-list class="pl-2" shaped>
      <v-list-item v-for="n in 5" :key="n" link>
        <v-list-item-action>
          <v-checkbox v-model="selected"></v-checkbox>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>Item {{ n }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
import CurrentTime from "../CurrentTime";

export default {
  components: { CurrentTime },
  data() {
    return {
      selected: true,
    };
  },
};
</script>
