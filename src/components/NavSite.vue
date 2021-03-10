<template>
  <div>
    <v-list class="pl-2" shaped v-for="(item, index) in data" :key="index">
      <NavSiteList
        :idx="index"
        :siteName="item.siteName"
        :status="item.status"
      ></NavSiteList>
    </v-list>
  </div>
</template>

<script>
import NavSiteList from "./NavSiteList";

export default {
  name: "NavSite",
  components: { NavSiteList },
  props: ["data"],
};
</script>
