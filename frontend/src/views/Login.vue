<template>
  <v-row justify="center">
    <v-col cols="4">
      <v-card>
        <v-card-title>Login</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="login">
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
import axios from '../axiosConfig';

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
    async login() {
      try {
        this.setCSRF();
        const user = await axios.post('/api/login/', this.loginForm);
        console.log(user);
      } catch (e) {
        console.log(e);
      }
    },
    setCSRF() {
      axios.get('/api/set-csrf-cookie/').then((res) => console.log(res));
    },
  },
};
</script>

<style scoped>

</style>
