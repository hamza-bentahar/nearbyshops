<template>
  <v-app>
    <top-bar></top-bar>
    <v-main>
      <v-container>
        <router-view/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import TopBar from './components/TopBar.vue';

export default {
  name: 'App',
  components: {
    TopBar,
  },
};
</script>
