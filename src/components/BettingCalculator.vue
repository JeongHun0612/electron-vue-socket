<template>
  <v-flex>
    <v-card height="200px">
      <div class="overseas-wdl">
        <span> {{ name }}</span>
      </div>
      <div class="">
        <span> {{ name }} {{ }} {{ }}</span>
      </div>
    </v-card>
  </v-flex>
</template>
<script>
export default {
  props: ["name"],
};
</script>

<style>
  .overseas-wdl {
    background-color: gray;
    text-align: center;
  }
</style>