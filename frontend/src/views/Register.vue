<template>
  <v-row justify="center">
    <v-col cols="4">
      <v-card>
        <v-card-title>Register</v-card-title>
        <v-card-text>
          <validation-observer ref="observer" v-slot="{ invalid }">
            <v-form @submit.prevent="register">
              <base-input v-model="registerForm.username"
                          rules="required"
                          name="username"
                          label="Username" />
              <base-input v-model="registerForm.email"
                          rules="required|email"
                          name="email"
                          label="Email" />
              <base-input
                v-model="registerForm.password"
                rules="required|min:8"
                name="password"
                type="password"
                label="Password"
              />
              <base-input
                v-model="registerForm.password_confirmation"
                rules="required|min:8|confirmed:password"
                name="password_confirmation"
                type="password"
                label="Password Confirmation"
              />
              <v-btn type="submit" color="primary" block :disabled="invalid" :loading="load">
                Register
              </v-btn>
            </v-form>
          </validation-observer>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { ValidationObserver } from 'vee-validate';
import { mapMutations } from 'vuex';
import BaseInput from '../components/BaseInput.vue';
import axios from '../axiosConfig';

export default {
  name: 'Register',
  components: {
    ValidationObserver,
    BaseInput,
  },
  data() {
    return {
      load: false,
      registerForm: {
        username: '',
        email: '',
        password: '',
        password_confirmation: '',
        first_name: '',
        last_name: '',
      },
    };
  },
  methods: {
    ...mapMutations(['DISPLAY_SNACKBAR']),
    async register() {
      try {
        await axios.post('/api/register/', this.registerForm);
        this.DISPLAY_SNACKBAR({ content: 'Registration Successful', color: 'success' });
        await this.$router.push('/login');
      } catch (e) {
        if (e.response && e.response.status === 400) {
          this.$refs.observer.setErrors(e.response.data);
        }
      }
    },
  },
};
</script>

<style scoped>

</style>
