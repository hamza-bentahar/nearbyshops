<template>
  <v-row justify="center">
    <v-col cols="4">
      <v-card>
        <v-card-title>Login</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="userLogin">
            <v-text-field v-model="loginForm.username" label="Username" type="username" />
            <v-text-field
              v-model="loginForm.password"
              label="Password"
              type="password"
              :error-messages="errorMessages" />
            <v-btn block color="primary" type="submit" :loading="load">
              Login
            </v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Login',
  data() {
    return {
      load: false,
      loginForm: {
        username: '',
        password: '',
      },
      errorMessages: '',
    };
  },
  methods: {
    ...mapActions(['login']),
    async userLogin() {
      try {
        await this.login(this.loginForm);
        await this.$router.push({ name: 'Home' });
      } catch (e) {
        this.errorMessages = e.response.data.detail;
      }
    },
  },
};
</script>

<style scoped>

</style>
