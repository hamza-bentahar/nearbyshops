import Vue from 'vue';
import Vuex from 'vuex';
import axios from '../axiosConfig';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    authenticated: false,
    user: null,
  },
  mutations: {
    SET_AUTHENTICATED: (state, value) => {
      state.authenticated = value;
    },
    SET_USER: (state, value) => {
      state.user = value;
    },
  },
  actions: {
    async logout({ commit }) {
      await axios.get('/api/logout/');
      commit('SET_AUTHENTICATED', false);
      commit('SET_USER', null);
    },
    async login({ commit, dispatch }, payload) {
      try {
        await dispatch('setCsrf');
        const isAuth = await axios.post('/api/login/', payload);
        if (isAuth.data.detail === 'authenticated') {
          commit('SET_AUTHENTICATED', true);
          commit('SET_USER', isAuth.data.user);
        }
      } catch (e) {
        console.log(e);
      }
    },
    async setCsrf() {
      try {
        await axios.get('/api/set-csrf-cookie/');
      } catch (e) {
        console.log(e);
      }
    },
    async checkAuthentication({ commit }) {
      try {
        const isAuth = await axios.get('/api/isauthenticated/');
        if (isAuth.data.detail === 'authenticated') {
          commit('SET_AUTHENTICATED', true);
          commit('SET_USER', isAuth.data.user);
        }
      } catch (e) {
        console.log(e);
      }
    },
  },
});
