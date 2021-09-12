<template>
  <div>
    <snackbar></snackbar>
    <v-app-bar app color="primary">
      <div class="d-flex align-center">
        <router-link to="/">
          <v-img
            alt="Vuetify Logo"
            class="shrink mr-2"
            contain
            src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
            transition="scale-transition"
            width="40"
          />
        </router-link>
      </div>

      <v-spacer></v-spacer>
      <div v-if="!isAuthenticated">
        <v-btn to="/login" raised elevation="4" class="ma-3">Login</v-btn>
        <v-btn to="/register" raised elevation="4" class="ma-3">Register</v-btn>
      </div>
      <div v-else>
        <v-btn @click="logout" raised elevation="4" class="ma-3">Logout</v-btn>
      </div>
    </v-app-bar>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import Snackbar from './Snackbar.vue';

export default {
  name: 'TopBar',
  components: {
    Snackbar,
  },
  computed: {
    ...mapGetters(['isAuthenticated']),
  },
  methods: {
    ...mapActions(['logout']),
  },
};
</script>

<style scoped>

</style>
